from __future__ import annotations

import os
import hashlib
from typing import TypedDict, Literal

from langgraph.graph import StateGraph, END

from config import GROQ_API_KEY, CONFIDENCE_THRESHOLD, ESCALATION_KEYWORDS
from retriever import get_retriever


class GraphState(TypedDict):
    query: str
    intent: str
    chunks: list
    confidence: str
    route: str
    llm_response: str
    final_answer: str
    escalated: bool
    escalation_reason: str
    human_response: str
    sources: list


def _extract_key_info(prompt: str) -> str:
    if "KNOWLEDGE BASE CONTEXT:" in prompt:
        start = prompt.find("KNOWLEDGE BASE CONTEXT:") + len("KNOWLEDGE BASE CONTEXT:")
        end = prompt.find("CUSTOMER QUERY:")
        return prompt[start:end].strip()[:300]
    return "No context found."


def _demo_llm_response(prompt: str) -> str:
    context = _extract_key_info(prompt)
    return (
        f"Based on our SwiftCart support documentation:\n\n"
        f"{context}\n\n"
        f"[Demo Mode: Add GROQ_API_KEY for real LLM responses]"
    )


def get_llm_response(prompt: str) -> str:
    if not GROQ_API_KEY:
        return _demo_llm_response(prompt)

    try:
        from groq import Groq
        client = Groq(api_key=GROQ_API_KEY)

        res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=500,
        )

        return res.choices[0].message.content.strip()

    except Exception as e:
        return f"[LLM Error] {str(e)}"


def build_prompt(query: str, context: str) -> str:
    return f"""
You are a helpful customer support agent for SwiftCart.

Use ONLY the context below.

KNOWLEDGE BASE CONTEXT:
{context}

CUSTOMER QUERY:
{query}

Answer clearly and concisely:
"""


def detect_intent(query: str) -> str:
    q = query.lower()

    if any(k in q for k in [x.lower() for x in ESCALATION_KEYWORDS]):
        return "escalation"

    if any(w in q for w in ["track", "order", "delivery"]):
        return "order_tracking"

    if any(w in q for w in ["refund", "payment", "charged", "bill"]):
        return "payment_issue"

    if any(w in q for w in ["return", "exchange"]):
        return "returns"

    if any(w in q for w in ["account", "password", "login"]):
        return "account"

    return "general"


def input_node(state: GraphState) -> GraphState:
    query = state["query"].strip()
    intent = detect_intent(query)
    return {**state, "intent": intent, "query": query}


def route_query(state: GraphState) -> Literal["rag_node", "hitl_node"]:
    intent = state["intent"]
    query = state["query"]

    retriever = get_retriever()
    _, confidence = retriever.retrieve_with_confidence(query)

    state["confidence"] = confidence

    if intent == "escalation" or confidence == "LOW":
        state["escalation_reason"] = f"{intent} / low confidence"
        return "hitl_node"

    return "rag_node"


def rag_node(state: GraphState) -> GraphState:
    retriever = get_retriever()
    chunks, confidence = retriever.retrieve_with_confidence(state["query"])

    context = retriever.format_context(chunks)
    prompt = build_prompt(state["query"], context)

    response = get_llm_response(prompt)

    sources = [f"Page {c['page']} (score {c['score']})" for c in chunks]

    return {
        **state,
        "chunks": chunks,
        "confidence": confidence,
        "llm_response": response,
        "sources": sources,
        "escalated": False
    }


def hitl_node(state: GraphState) -> GraphState:
    ticket = f"SC-{hashlib.md5(state['query'].encode()).hexdigest()[:6].upper()}"

    response = f"""
Your request has been escalated to a human agent.

Ticket ID: {ticket}
Response time: 2–4 hours
"""

    return {
        **state,
        "llm_response": response,
        "escalated": True,
        "chunks": [],
        "sources": []
    }


def output_node(state: GraphState) -> GraphState:
    answer = state["llm_response"]

    if state.get("sources") and not state["escalated"]:
        answer += "\n\nSources:\n" + "\n".join(state["sources"][:3])

    return {**state, "final_answer": answer}


def build_graph():
    graph = StateGraph(GraphState)

    graph.add_node("input_node", input_node)
    graph.add_node("rag_node", rag_node)
    graph.add_node("hitl_node", hitl_node)
    graph.add_node("output_node", output_node)

    graph.set_entry_point("input_node")

    graph.add_conditional_edges(
        "input_node",
        route_query,
        {
            "rag_node": "rag_node",
            "hitl_node": "hitl_node"
        }
    )

    graph.add_edge("rag_node", "output_node")
    graph.add_edge("hitl_node", "output_node")
    graph.add_edge("output_node", END)

    return graph.compile()


_graph = None

def get_graph():
    global _graph
    if _graph is None:
        _graph = build_graph()
    return _graph


def run_query(query: str):
    graph = get_graph()

    state: GraphState = {
        "query": query,
        "intent": "",
        "chunks": [],
        "confidence": "",
        "route": "",
        "llm_response": "",
        "final_answer": "",
        "escalated": False,
        "escalation_reason": "",
        "human_response": "",
        "sources": []
    }

    return graph.invoke(state)
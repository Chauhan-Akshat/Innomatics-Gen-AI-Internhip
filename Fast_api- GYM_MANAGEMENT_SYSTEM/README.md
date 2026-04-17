# 🏋️ Golds Gym API

### 🚀 Advanced FastAPI Backend for Gym Management

**Author: Akshat**

---

## 📌 Overview

Golds Gym API is a fully-featured backend system built using **FastAPI**, designed to simulate a real-world gym membership and class management platform.

This project goes beyond basic CRUD — it incorporates:

* Business logic (pricing, discounts, referrals)
* Membership lifecycle management
* Class booking workflows
* Advanced filtering, search, sorting, and pagination

It’s structured to reflect how production-grade backend systems are built.

---

## ⚙️ Tech Stack

* **Backend Framework:** FastAPI
* **Language:** Python
* **Validation:** Pydantic
* **Server:** Uvicorn

---

## 🧠 Core Features

### 📦 Plan Management

* Create, update, delete gym plans
* Filter by price, duration, trainer, classes
* Search by keyword
* Sort and paginate plans
* Smart browsing with combined filters

---

### 👤 Membership System

* Enroll users into plans
* Automatic pricing engine:

  * Duration-based discounts (10% / 20%)
  * Referral discount (5%)
  * EMI processing fee
* Freeze and reactivate memberships
* Search, sort, and paginate memberships

---

### 🏃 Class Booking System

* Book fitness classes
* Validates:

  * Active membership
  * Plan includes classes
* Cancel bookings
* Track all bookings

---

### 🔍 Advanced API Features

* Combined filtering + sorting + pagination
* Clean validation using Pydantic
* Error handling using HTTPException
* Query parameter handling with optional filters

---

## 📂 Project Structure

```
main.py
README.md
```

Everything is implemented in a single file for simplicity and clarity.

---

## 🚀 Getting Started

### 1️⃣ Install Dependencies

```bash
pip install fastapi uvicorn
```

### 2️⃣ Run Server

```bash
uvicorn main:app --reload
```

### 3️⃣ Open API Docs

* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

---

## 📡 API Endpoints

### 🏠 Basic

* `GET /` → Welcome message

---

### 📊 Plans

* `GET /plans` → Get all plans
* `GET /plans/{id}` → Get plan by ID
* `GET /plans/summary` → Plan analytics
* `GET /plans/filter` → Filter plans
* `POST /plans` → Create plan
* `PUT /plans/{id}` → Update plan
* `DELETE /plans/{id}` → Delete plan

---

### 🔎 Advanced Plan APIs

* `GET /plans/search`
* `GET /plans/sort`
* `GET /plans/page`
* `GET /plans/browse`

---

### 👥 Memberships

* `GET /memberships`
* `POST /memberships`
* `PUT /memberships/{id}/freeze`
* `PUT /memberships/{id}/reactivate`

---

### 🔍 Membership Utilities

* `GET /memberships/search`
* `GET /memberships/sort`
* `GET /memberships/page`

---

### 🏋️ Classes

* `POST /classes/book`
* `GET /classes/bookings`
* `DELETE /classes/cancel/{id}`

---

## 💡 Business Logic Highlights

### 💰 Pricing Engine

* 6+ months → 10% discount
* 12+ months → 20% discount
* Referral code → extra 5% discount
* EMI → ₹200 processing fee

### 🔐 Validation

* Phone must be at least 10 digits
* Plan must exist before enrollment
* Cannot delete plan with active members
* Only active members with class-enabled plans can book classes

---

## 🧪 Sample Request

### Create Membership

```json
POST /memberships

{
  "member_name": "Akshat",
  "plan_id": 3,
  "phone": "9876543210",
  "start_month": "March",
  "payment_mode": "emi",
  "referral_code": "FIT5"
}
```

---

## 📈 Future Improvements

* Database integration (PostgreSQL / MongoDB)
* JWT Authentication & Role-based access
* Payment gateway integration
* Admin dashboard
* Real-time class slots tracking
* Deployment with Docker & CI/CD

---

## 🎯 Why This Project Stands Out

This isn’t just a practice API — it demonstrates:

* Clean architecture thinking
* Real-world business logic implementation
* Scalable endpoint design
* Strong understanding of backend fundamentals

---

## 📜 License

Open-source project for learning and development purposes.

---

## 🙌 Final Note

Built with a focus on clarity, scalability, and real-world applicability.
A solid foundation for any production-grade backend system.

---

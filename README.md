
**backend software developer** for **Murang’a National Hospital**. You are required to build a **user authentication system** for the hospital’s internal portal.

The system should allow hospital staff to:

1. **Register** a new user with a username, email, and password.
2. **Login** with email and password.
3. **Access protected routes** using JWT-based authentication.
4. **Securely store passwords** in a PostgreSQL database.
5. **Log all API requests** using middleware (method, path, status code, response time).
6. **Trigger background tasks** when a user registers (e.g., simulate sending a welcome email).

You are required to:

* Use **FastAPI** to implement the API.
* Use **Pydantic** models for input validation.
* Use **psycopg2** to connect to PostgreSQL.
* Use **python-jose[cryptography]** for JWT tokens.
* Use **passlib[bcrypt]** for password hashing.
* Implement modular code (separate files for database, authentication, middleware, and JWT handling).

**Deliverables:**

* A working FastAPI project with the endpoints:

  * `POST /auth/register` → Register user
  * `POST /auth/login` → Login user and return JWT
  * `GET /auth/me` → Return current user (JWT protected)
* Middleware logs of requests.
* Background task simulation for registration.



# **FastAPI JWT Authentication System**

## **Project Overview**

This project is a **FastAPI-based authentication module** for web and mobile applications.
It demonstrates:

* User registration and login
* JWT-based authentication
* Middleware logging
* Background tasks
* PostgreSQL integration for user storage

This project is intended as **Day 2 practical assignment** for learning FastAPI, JWT auth, and backend best practices.

---

## **Features**

* **User Registration:** Users can register with a username, email, and password. Passwords are securely hashed using bcrypt.
* **User Login:** Authenticates users and returns a JWT access token.
* **Protected Routes:** Routes like `/auth/me` require a valid JWT token.
* **Middleware:** Logs HTTP method, request path, response status, and request duration.
* **Background Tasks:** Simulates sending welcome emails after user registration.
* **Database:** PostgreSQL stores user data.
* **Pydantic Models:** Input validation and response schemas.

---

## **Technologies Used**

* **Python 3.11+**
* **FastAPI** – Web framework
* **PostgreSQL** – Relational database
* **psycopg2-binary** – PostgreSQL connector
* **python-jose[cryptography]** – JWT creation and validation
* **passlib[bcrypt]** – Password hashing
* **python-multipart** – Handling form data for FastAPI
* **Pydantic** – Data validation and serialization
* **Uvicorn** – ASGI server

---

## **Project Structure**

```
jwt_Auth/
pyproject.tmol
RedMe.md
app/
│── main.py                
 

---

## **Setup Instructions**

### 1. Clone the repository

```bash
git clone <repo-url>
cd project
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Dependencies include:

* fastapi
* uvicorn
* psycopg2-binary
* passlib[bcrypt]
* python-jose[cryptography]
* python-multipart

### 4. Configure PostgreSQL

1. Create a database:

```sql
CREATE DATABASE fastapi_auth;
```

2. Create users table:

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
```

3. Update `database.py` with your PostgreSQL credentials.

---

### 5. Run the server

```bash
uvicorn main:app --reload
```

* FastAPI docs available at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## **Usage**

1. **Register a user**

   * Endpoint: `POST /auth/register`
   * Payload: `{ "username": "user1", "email": "user1@example.com", "password": "mypassword" }`

2. **Login**

   * Endpoint: `POST /auth/login`
   * Payload: `{ "email": "user1@example.com", "password": "mypassword" }`
   * Response: JWT token

3. **Access protected route**

   * Endpoint: `GET /auth/me`
   * Header: `Authorization: Bearer <JWT_TOKEN>`

4. **Check middleware logs**

   * Logs HTTP method, path, status code, and duration in terminal.

5. **Background tasks**

   * On registration, simulates sending a welcome email (printed in terminal or logged to file).

---

## **Learning Outcomes**

By completing this project, you will learn:

* How to use FastAPI with PostgreSQL
* Implement JWT-based authentication
* Middleware creation in FastAPI
* Background task handling
* Pydantic for request validation
* Structuring a modular backend project

---

## **License**

MIT License



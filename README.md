📊 AttendanceApp – Smart Attendance Management System

📑 Table of Contents

Overview

Features

Tech Stack

Architecture

Project Structure

Installation

Running the Application

API Endpoints

Database Schema

Example API Response

Environment Variables

Deployment

Future Improvements

Contributing

Author

License








📌 Overview

AttendanceApp is a lightweight backend system built using Python and FastAPI to manage student attendance efficiently.

The application allows users to store, track, and manage attendance records using a simple API structure and a SQLite database.

This project demonstrates backend development concepts such as:

REST API development

Database integration

Server deployment

Python backend architecture

🚀 Features

✅ Student attendance tracking
✅ FastAPI backend API
✅ SQLite database integration
✅ Lightweight and easy to run
✅ RESTful API endpoints


🛠 Tech Stack

Backend: Python

Framework: FastAPI

Server: Uvicorn

Database: SQLite

Version Control: Git & GitHub

🏗 Architecture
Client Request
      ↓
FastAPI Routes (main.py)
      ↓
Database Layer (database.py)
      ↓
SQLite Database (attendance.db)
      ↓
API Response

📂 Project Structure
AttendanceApp
│
├── AttendanceApp/        # Application modules
├── main.py               # Main FastAPI application
├── database.py           # Database connection and logic
├── attendance.db         # SQLite database file
├── requirements.txt      # Project dependencies
├── .gitignore            # Ignored files
└── README.md             # Project documentation

⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/amartya69/AttendanceApp.git

2️⃣ Navigate to Project Folder
cd AttendanceApp

3️⃣ Create Virtual Environment
python -m venv venv

Activate environment

Windows

venv\Scripts\activate

Mac / Linux

source venv/bin/activate

4️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Running the Application

Start the FastAPI server:

uvicorn main:app --reload

Server will run at:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs

📡 API Endpoints
Method	Endpoint	Description
GET	/attendance	Get attendance records
POST	/attendance	Add attendance
GET	/students	Get student list

(Modify based on your actual endpoints)

🗄 Database Schema

Example attendance table structure:

Column	Type
id	INTEGER
student_name	TEXT
date	TEXT
status	TEXT


📡 Example API Endpoint

Example request:

GET /attendance

Example response:

{
  "student_id": 1,
  "name": "John Doe",
  "status": "Present"
}

🔐 Environment Variables

If required, create a .env file:

DATABASE_URL=sqlite:///attendance.db

☁️ Deployment

This project can be deployed using:

Render

Railway

Heroku

Docker

Example Render command:
uvicorn main:app --host 0.0.0.0 --port 10000

🎯 Project Goals

The main objective of this project is to build a simple backend system that demonstrates how attendance data can be stored and managed using REST APIs.

Goals of the project:

Understand backend development using FastAPI

Learn database integration with SQLite

Build and test RESTful APIs

Practice structuring a Python backend project

Deploy a backend service on cloud platforms

📊 System Workflow

The workflow of the AttendanceApp is:

User Request
     ↓
FastAPI Endpoint
     ↓
Business Logic
     ↓
Database Query
     ↓
SQLite Database
     ↓
Response Returned to Client

🔍 API Documentation

FastAPI automatically generates interactive API documentation.

You can access it here after running the server:

Swagger UI

http://127.0.0.1:8000/docs

ReDoc Documentation

http://127.0.0.1:8000/redoc

These interfaces allow developers to test API endpoints directly from the browser.

🧪 Testing the API

You can test the API using the following tools:

Swagger UI (built-in with FastAPI)

Postman

cURL

Example using cURL:

curl http://127.0.0.1:8000/attendance

Example using Postman:

Open Postman

Create a new request

Use endpoint GET /attendance

Send request and view response

📁 Dependency Management

All project dependencies are listed in the requirements.txt file.

Example dependencies:

fastapi
uvicorn
pydantic
sqlite3

Install them using:
pip install -r requirements.txt

🛡 Error Handling

The application includes basic error handling for:

Invalid API requests

Database connection errors

Missing parameters

FastAPI automatically returns appropriate HTTP responses such as:

200 OK

400 Bad Request

404 Not Found

500 Internal Server Error

📦 Deployment Ready

This project is ready for deployment on cloud platforms such as:

Render

Railway

Heroku

Docker containers

Deployment command example:
uvicorn main:app --host 0.0.0.0 --port 10000

🔧 Development Setup

Recommended development tools:

Tool	Purpose
VS Code	Code Editor
Python 3.9+	Runtime
Git	Version Control
Postman	API Testing

Recommended VS Code extensions:

Python

Pylance

REST Client

📈 Future Improvements

Authentication system

Web-based dashboard

Analytics for attendance

Student management system

📜 License

This project is open-source and available under the MIT License.

Cloud database support


👨‍💻 Author

Amartya Prakash

Backend Developer

Interested in Python, Java, and API Development

Building projects to improve software development skills

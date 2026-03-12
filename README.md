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

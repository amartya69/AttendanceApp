# main.py
from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional
from database import initialize_db, execute_query, fetch_all

# -----------------------
# FastAPI App Metadata
# -----------------------
app = FastAPI(
    title="Automated Student Attendance System",
    description="""
    🚀 **Smart India Hackathon Project**  
    This system manages student attendance with real-time analytics.  

    👥 **Team Name**: Hack Forge
    """,
    version="1.0.0"
)

# -----------------------
# Initialize Database
# -----------------------
initialize_db()

# -----------------------
# Pydantic Models
# -----------------------
class Student(BaseModel):
    name: str
    roll_no: str
    department: str
    email: EmailStr

class Attendance(BaseModel):
    student_id: str
    date: str
    status: str  # "Present" or "Absent"

# -----------------------
# Routes
# -----------------------
@app.get("/", tags=["Home"])
def home():
    return {"message": "Welcome to the Automated Student Attendance System 🚀"}

# Add Student
@app.post("/students", tags=["Students"])
def add_student(student: Student):
    query = "INSERT INTO students (name, roll_no, department, email) VALUES (?, ?, ?, ?)"
    execute_query(query, (student.name, student.roll_no, student.department, student.email))
    return {"message": "✅ Student added successfully", "student": student.dict()}

# Get All Students (optional filters)
@app.get("/students", tags=["Students"])
def get_students(
    department: Optional[str] = Query(None, description="Filter by department"),
    roll_no: Optional[str] = Query(None, description="Search by roll number"),
):
    query = "SELECT * FROM students WHERE 1=1"
    params = []

    if department:
        query += " AND department = ?"
        params.append(department)
    if roll_no:
        query += " AND roll_no = ?"
        params.append(roll_no)

    students = fetch_all(query, params)
    return {"students": [dict(student) for student in students]}

# Mark Attendance
@app.post("/attendance", tags=["Attendance"])
def mark_attendance(attendance: Attendance):
    # Check if student exists
    student_check = fetch_all("SELECT * FROM students WHERE roll_no = ?", (attendance.student_id,))
    if not student_check:
        raise HTTPException(status_code=404, detail="Student not found")

    query = "INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)"
    execute_query(query, (attendance.student_id, attendance.date, attendance.status))
    return {"message": "✅ Attendance marked!", "attendance": attendance.dict()}

# Get Attendance Report
@app.get("/attendance/report/{roll_no}", tags=["Attendance"])
def get_attendance_report(
    roll_no: str,
    start_date: Optional[str] = Query(None, description="Start date (YYYY-MM-DD)"),
    end_date: Optional[str] = Query(None, description="End date (YYYY-MM-DD)"),
):
    query = "SELECT * FROM attendance WHERE student_id = ?"
    params = [roll_no]

    if start_date and end_date:
        query += " AND date BETWEEN ? AND ?"
        params.extend([start_date, end_date])

    records = fetch_all(query, params)
    total = len(records)
    present = sum(1 for r in records if r["status"] == "Present")

    return {
        "student_id": roll_no,
        "total_days": total,
        "present_days": present,
        "attendance_percentage": f"{(present/total*100) if total > 0 else 0:.2f}%"
    }

# Daily Attendance Analytics
@app.get("/attendance/daily", tags=["Analytics"])
def daily_attendance(date: str = Query(..., description="Date (YYYY-MM-DD)")):
    records = fetch_all("SELECT * FROM attendance WHERE date = ?", (date,))
    total = len(records)
    present = sum(1 for r in records if r["status"] == "Present")
    absent = total - present

    return {
        "date": date,
        "total_students": total,
        "present": present,
        "absent": absent,
        "attendance_percentage": f"{(present/total*100) if total > 0 else 0:.2f}%"
    }

# -----------------------
# Optional: Test User Data
# -----------------------
if __name__ == "__main__":
    # Insert a test user for local testing
    execute_query("INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)", 
                  ("Amartya", "amartya@example.com"))

    users = fetch_all("SELECT * FROM users")
    for user in users:
        print(dict(user))


# add superadmin code in backend

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Temporary in-memory storage (replace with DB later)
admins = []

# Request body model
class Admin(BaseModel):
    email: str
    password: str
    college: str

@app.post("/api/admins")
def create_admin(admin: Admin):
    if not admin.email or not admin.password or not admin.college:
        return {"success": False, "message": "All fields are required"}

    # Later you’ll save this in a database
    admins.append(admin.dict())

    return {"success": True, "message": "Admin created successfully!"}

@app.get("/api/admins", response_model=List[Admin])
def get_admins():
    return admins

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 👇 Add your Vercel frontend URL here
origins = [
    "https://attendance-frontend.vercel.app",  # your Vercel frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend is working!"}


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://attendance-frontend-two-neon.vercel.app/",   # <- exact Vercel URL
    "http://localhost:3000",              # optional, for local dev
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

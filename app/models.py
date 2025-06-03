from datetime import datetime
from app.database import db

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    submitted_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Department(BaseModel):
    __tablename__ = 'departments'
    department_name = db.Column(db.String(100), nullable=False)

class Course(BaseModel):
    __tablename__ = 'courses'
    course_name = db.Column(db.String(100), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)
    semester = db.Column(db.String(20))
    class_name = db.Column(db.String(20))
    lecture_hours = db.Column(db.Integer)

class Student(BaseModel):
    __tablename__ = 'students'
    full_name = db.Column(db.String(100), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)
    class_name = db.Column(db.String(20))

class AttendanceLog(BaseModel):
    __tablename__ = 'attendance_log'
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    present = db.Column(db.Boolean, nullable=False)

class User(BaseModel):
    __tablename__ = 'users'
    type = db.Column(db.String(20), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

from flask import Blueprint, request, jsonify
from models import db, Student

student_bp = Blueprint('student_bp', __name__)

@student_bp.route('/', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{"id": s.id, "name": s.name, "email": s.email} for s in students])

@student_bp.route('/', methods=['POST'])
def add_student():
    data = request.json
    student = Student(name=data['name'], email=data['email'])
    db.session.add(student)
    db.session.commit()
    return jsonify({"message": "Student added", "id": student.id}), 201

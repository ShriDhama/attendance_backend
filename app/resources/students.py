from flask_restful import Resource, reqparse
from app.models import Student
from app.database import db

parser = reqparse.RequestParser()
parser.add_argument('full_name', required=True)
parser.add_argument('department_id', type=int, required=True)
parser.add_argument('class_name')
parser.add_argument('submitted_by', type=int)

class StudentListResource(Resource):
    def get(self):
        students = Student.query.all()
        return [{'id': s.id, 'full_name': s.full_name, 'class_name': s.class_name} for s in students]

    def post(self):
        args = parser.parse_args()
        student = Student(**args)
        db.session.add(student)
        db.session.commit()
        return {'id': student.id, 'message': 'Student created'}, 201

class StudentResource(Resource):
    def get(self, id):
        student = Student.query.get_or_404(id)
        return {'id': student.id, 'full_name': student.full_name, 'class_name': student.class_name}

    def put(self, id):
        args = parser.parse_args()
        student = Student.query.get_or_404(id)
        student.full_name = args['full_name']
        student.department_id = args['department_id']
        student.class_name = args['class_name']
        student.submitted_by = args['submitted_by']
        db.session.commit()
        return {'message': 'Student updated'}

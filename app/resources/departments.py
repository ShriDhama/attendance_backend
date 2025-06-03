from flask_restful import Resource, reqparse
from app.models import Department
from app.database import db

parser = reqparse.RequestParser()
parser.add_argument('department_name', required=True)
parser.add_argument('submitted_by', type=int)

class DepartmentListResource(Resource):
    def get(self):
        departments = Department.query.all()
        return [{'id': d.id, 'department_name': d.department_name} for d in departments]

    def post(self):
        args = parser.parse_args()
        department = Department(**args)
        db.session.add(department)
        db.session.commit()
        return {'id': department.id, 'message': 'Department created'}, 201

class DepartmentResource(Resource):
    def get(self, id):
        department = Department.query.get_or_404(id)
        return {'id': department.id, 'department_name': department.department_name}

    def put(self, id):
        args = parser.parse_args()
        department = Department.query.get_or_404(id)
        department.department_name = args['department_name']
        department.submitted_by = args['submitted_by']
        db.session.commit()
        return {'message': 'Department updated'}

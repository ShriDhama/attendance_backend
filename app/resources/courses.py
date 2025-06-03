from flask_restful import Resource, reqparse
from app.models import Course
from app.database import db

parser = reqparse.RequestParser()
parser.add_argument('course_name', required=True)
parser.add_argument('department_id', type=int, required=True)
parser.add_argument('semester')
parser.add_argument('class_name')
parser.add_argument('lecture_hours', type=int)
parser.add_argument('submitted_by', type=int)

class CourseListResource(Resource):
    def get(self):
        courses = Course.query.all()
        return [{'id': c.id, 'course_name': c.course_name} for c in courses]

    def post(self):
        args = parser.parse_args()
        course = Course(**args)
        db.session.add(course)
        db.session.commit()
        return {'id': course.id, 'message': 'Course created'}, 201

class CourseResource(Resource):
    def get(self, id):
        course = Course.query.get_or_404(id)
        return {'id': course.id, 'course_name': course.course_name}

    def put(self, id):
        args = parser.parse_args()
        course = Course.query.get_or_404(id)
        course.course_name = args['course_name']
        course.department_id = args['department_id']
        course.semester = args['semester']
        course.class_name = args['class_name']
        course.lecture_hours = args['lecture_hours']
        course.submitted_by = args['submitted_by']
        db.session.commit()
        return {'message': 'Course updated'}

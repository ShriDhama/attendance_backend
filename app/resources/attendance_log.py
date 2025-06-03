from flask_restful import Resource, reqparse
from app.models import AttendanceLog
from app.database import db

parser = reqparse.RequestParser()
parser.add_argument('student_id', type=int, required=True)
parser.add_argument('course_id', type=int, required=True)
parser.add_argument('present', type=bool, required=True)
parser.add_argument('submitted_by', type=int)

class AttendanceLogListResource(Resource):
    def get(self):
        logs = AttendanceLog.query.all()
        return [{'id': log.id, 'student_id': log.student_id, 'course_id': log.course_id, 'present': log.present} for log in logs]

    def post(self):
        args = parser.parse_args()
        log = AttendanceLog(**args)
        db.session.add(log)
        db.session.commit()
        return {'id': log.id, 'message': 'Attendance log created'}, 201

class AttendanceLogResource(Resource):
    def get(self, id):
        log = AttendanceLog.query.get_or_404(id)
        return {'id': log.id, 'student_id': log.student_id, 'course_id': log.course_id, 'present': log.present}

    def put(self, id):
        args = parser.parse_args()
        log = AttendanceLog.query.get_or_404(id)
        log.student_id = args['student_id']
        log.course_id = args['course_id']
        log.present = args['present']
        log.submitted_by = args['submitted_by']
        db.session.commit()
        return {'message': 'Attendance log updated'}

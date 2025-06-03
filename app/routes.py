from flask_restful import Api
from app.resources.departments import DepartmentListResource, DepartmentResource
from app.resources.courses import CourseListResource, CourseResource
from app.resources.students import StudentListResource, StudentResource
from app.resources.attendance_log import AttendanceLogListResource, AttendanceLogResource
from app.resources.users import UserListResource, UserResource, UserLoginResource

def register_routes(app):
    api = Api(app)
    api.add_resource(DepartmentListResource, '/departments')
    api.add_resource(DepartmentResource, '/departments/<int:id>')
    api.add_resource(CourseListResource, '/courses')
    api.add_resource(CourseResource, '/courses/<int:id>')
    api.add_resource(StudentListResource, '/students')
    api.add_resource(StudentResource, '/students/<int:id>')
    api.add_resource(AttendanceLogListResource, '/attendance_logs')
    api.add_resource(AttendanceLogResource, '/attendance_logs/<int:id>')
    api.add_resource(UserListResource, '/users')
    api.add_resource(UserResource, '/users/<int:id>')
    api.add_resource(UserLoginResource, '/login')

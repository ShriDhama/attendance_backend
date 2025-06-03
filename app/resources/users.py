from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from app.database import db

user_parser = reqparse.RequestParser()
user_parser.add_argument('type', required=True)
user_parser.add_argument('full_name', required=True)
user_parser.add_argument('username', required=True)
user_parser.add_argument('email', required=True)
user_parser.add_argument('password', required=True)
user_parser.add_argument('submitted_by', type=int)

login_parser = reqparse.RequestParser()
login_parser.add_argument('username', required=True)
login_parser.add_argument('password', required=True)

class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return [{'id': u.id, 'full_name': u.full_name, 'username': u.username} for u in users]

    def post(self):
        args = user_parser.parse_args()
        hashed_password = generate_password_hash(args['password'])
        user = User(type=args['type'], full_name=args['full_name'], username=args['username'],
                    email=args['email'], password=hashed_password, submitted_by=args['submitted_by'])
        db.session.add(user)
        db.session.commit()
        return {'id': user.id, 'message': 'User created'}, 201

class UserResource(Resource):
    def get(self, id):
        user = User.query.get_or_404(id)
        return {'id': user.id, 'full_name': user.full_name, 'username': user.username}

    def put(self, id):
        args = user_parser.parse_args()
        user = User.query.get_or_404(id)
        user.full_name = args['full_name']
        user.username = args['username']
        user.email = args['email']
        user.type = args['type']
        user.password = generate_password_hash(args['password'])
        db.session.commit()
        return {'message': 'User updated'}

class UserLoginResource(Resource):
    def post(self):
        args = login_parser.parse_args()
        user = User.query.filter_by(username=args['username']).first()
        if user and check_password_hash(user.password, args['password']):
            return {'message': 'Login successful', 'user_id': user.id}
        return {'message': 'Invalid credentials'}, 401

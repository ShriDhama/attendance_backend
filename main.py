from flask import Flask
from flask_migrate import Migrate
from app.database import db
from app.models import *
from app.routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    register_routes(app)

    # Add a root route to verify the API is running
    @app.route("/")
    def index():
        return {"message": "Attendance Management System API is running."}

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

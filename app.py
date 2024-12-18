from flask import Flask
from flask_smorest import Api
from db import db
import models
from resources.course_item import blp as CourseItemBlueprint
from resources.specialization import blp as SpecializationBlueprint

def create_app():
    app = Flask(__name__)

    # API Configurations
    app.config["API_TITLE"] = "TBS REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    # SQLite Configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True

    db.init_app(app)
    api = Api(app)

    # Register Blueprints
    api.register_blueprint(CourseItemBlueprint)
    api.register_blueprint(SpecializationBlueprint)

    with app.app_context():
        db.create_all()  # Create tables if not exist

    return app

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from models.specialization import SpecializationModel
from schemas import SpecializationSchema
from db import db

blp = Blueprint("Specializations", "specializations", description="Operations on specializations")

@blp.route("/specialization/<int:specialization_id>")
class Specialization(MethodView):
    @blp.response(200, SpecializationSchema)
    def get(self, specialization_id):
        return SpecializationModel.query.get_or_404(specialization_id)

    def delete(self, specialization_id):
        specialization = SpecializationModel.query.get_or_404(specialization_id)
        db.session.delete(specialization)
        db.session.commit()
        return {"message": "Specialization deleted."}

@blp.route("/specialization")
class SpecializationList(MethodView):
    @blp.response(200, SpecializationSchema(many=True))
    def get(self):
        return SpecializationModel.query.all()

    @blp.arguments(SpecializationSchema)
    @blp.response(201, SpecializationSchema)
    def post(self, specialization_data):
        specialization = SpecializationModel(**specialization_data)
        try:
            db.session.add(specialization)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Specialization with this name already exists.")
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the specialization.")
        return specialization

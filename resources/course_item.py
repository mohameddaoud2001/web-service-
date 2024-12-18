from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from models.course_item import CourseItemModel
from schemas import CourseItemSchema, CourseItemUpdateSchema
from db import db

blp = Blueprint("CourseItems", "course_items", description="Operations on course items")

@blp.route("/course_item/<int:course_item_id>")
class CourseItem(MethodView):
    @blp.response(200, CourseItemSchema)
    def get(self, course_item_id):
        return CourseItemModel.query.get_or_404(course_item_id)

    def delete(self, course_item_id):
        course_item = CourseItemModel.query.get_or_404(course_item_id)
        db.session.delete(course_item)
        db.session.commit()
        return {"message": "Course item deleted."}

    @blp.arguments(CourseItemUpdateSchema)
    @blp.response(200, CourseItemSchema)
    def put(self, course_item_data, course_item_id):
        course_item = CourseItemModel.query.get(course_item_id)
        if course_item:
            course_item.name = course_item_data["name"]
            course_item.type = course_item_data["type"]
        else:
            course_item = CourseItemModel(id=course_item_id, **course_item_data)
        db.session.add(course_item)
        db.session.commit()
        return course_item

@blp.route("/course_item")
class CourseItemList(MethodView):
    @blp.response(200, CourseItemSchema(many=True))
    def get(self):
        return CourseItemModel.query.all()

    @blp.arguments(CourseItemSchema)
    @blp.response(201, CourseItemSchema)
    def post(self, course_item_data):
        course_item = CourseItemModel(**course_item_data)
        try:
            db.session.add(course_item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the course item.")
        return course_item

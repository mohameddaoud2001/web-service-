from db import db

class CourseItemModel(db.Model):
    __tablename__ = "course_items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(80), nullable=False)
    specialization_id = db.Column(db.Integer, db.ForeignKey("specializations.id"), nullable=False)
    specialization = db.relationship("SpecializationModel", back_populates="courseitems")

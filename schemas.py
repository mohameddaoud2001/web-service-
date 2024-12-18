from marshmallow import Schema, fields

class PlainCourseItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    type = fields.Str(required=True)

class PlainSpecializationSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class CourseItemSchema(PlainCourseItemSchema):
    specialization_id = fields.Int(required=True, load_only=True)
    specialization = fields.Nested(PlainSpecializationSchema, dump_only=True)

class CourseItemUpdateSchema(Schema):
    name = fields.Str()
    type = fields.Str()

class SpecializationSchema(PlainSpecializationSchema):
    courseitems = fields.List(fields.Nested(PlainCourseItemSchema), dump_only=True)

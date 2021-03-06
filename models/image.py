from app import db, ma
from marshmallow import fields
from .base import BaseModel, BaseSchema
# pylint: disable=W0611
from .difficulty import Difficulty
from .user import User

# image model defines each project (has a relationship with the user who created it and the difficulty picked)
class ImageModel(db.Model, BaseModel):

    __tablename__ = 'images'

    title = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(300), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref='created_images')
    difficulty_id = db.Column(db.Integer, db.ForeignKey('difficulties.id'), nullable=False)
    difficulty = db.relationship('Difficulty', backref='created_images')

class ImageSchema(ma.ModelSchema, BaseSchema):

    class Meta:
        model = ImageModel

    pixels = fields.Nested('PixelSchema', many=True, exclude=('created_at', 'updated_at'))
    colors = fields.Nested('ColorSchema', many=True, exclude=('created_at', 'updated_at'))
    user = fields.Nested('UserSchema', only={'id', 'username'})
    difficulty = fields.Nested('DifficultySchema', only=('id', 'level', 'pixelSize'))
    notes = fields.Nested('NoteSchema', many=True)

# each image has an array of pixels, as the user ticks them on the front end the ticked boolean changes
class Pixel(db.Model, BaseModel):

    __tablename__ = 'pixels'

    color = db.Column(db.String(30), nullable=False)
    ticked = db.Column(db.Boolean, nullable=False)
    image_id = db.Column(db.Integer, db.ForeignKey('images.id'))
    image = db.relationship('ImageModel', backref='pixels')

class PixelSchema(ma.ModelSchema, BaseSchema):

    class Meta:
        model = Pixel

# each image has an array of the most commonly found colors in it.
# This also includes how many stiches are needed per color and the length of the thread needed
class Color(db.Model, BaseModel):

    __tablename__ = 'colors'

    color = db.Column(db.String(30), nullable=False)
    length = db.Column(db.Integer, nullable=False)
    stitches = db.Column(db.Integer, nullable=False)
    image_id = db.Column(db.Integer, db.ForeignKey('images.id'))
    image = db.relationship('ImageModel', backref='colors')

class ColorSchema(ma.ModelSchema, BaseSchema):

    class Meta:
        model = Color

# each image has an array of notes
class Note(db.Model, BaseModel):

    __tablename__ = 'notes'

    text = db.Column(db.String(300), nullable=False)
    image_id = db.Column(db.Integer, db.ForeignKey('images.id'))
    image = db.relationship('ImageModel', backref='notes')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='created_notes')

class NoteSchema(ma.ModelSchema, BaseSchema):

    class Meta:
        model = Note
    user = fields.Nested('UserSchema', only={'id', 'username'})

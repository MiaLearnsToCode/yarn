from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config.environment import db_uri
from flask_bcrypt import Bcrypt

app = Flask(__name__, static_folder='dist')
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)

# pylint: disable=C0413,W0611,C0412
from config import router

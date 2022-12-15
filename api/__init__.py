import os

from flask import Flask
from flask_cors import CORS

from api.routes import rest_api
from api.models import db
from api.routes import route_api

# Create App
app = Flask(__name__)

# load Config 
app.config.from_object('api.config.BaseConfig')

# Connect Flask and FlaskRestX
app.register_blueprint(route_api)

# Connect Flask and SqlAlchemy
db.init_app(app)


# rest_api.init_app(app)

# Enable CORS
CORS(app)

# Setup database
@app.before_first_request
def initialize_database():
    db.create_all()

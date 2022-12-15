from flask_restx import Api
from api.controller import data

from flask import Blueprint

route_api = Blueprint('api', __name__, url_prefix='/api/1')

rest_api = Api(route_api,version="1.0", title="Application API",doc='/docs',
    # base_url='/api'
    )

rest_api.add_namespace(data.rest_api)
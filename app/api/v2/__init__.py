from flask import Blueprint

v1 = Blueprint("apiv1", __name__, url_prefix="/api/v1")
v2 = Blueprint("apiv2", __name__, url_prefix="/api/v2")

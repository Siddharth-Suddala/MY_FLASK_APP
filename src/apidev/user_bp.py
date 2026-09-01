from flask import Blueprint
from flask import Flask

user_bp = Blueprint("user_bp",__name__,url_prefix="/user")


@user_bp.route("/test")
def handle_test():
    return "HELLO FROM BLUEPRINT"



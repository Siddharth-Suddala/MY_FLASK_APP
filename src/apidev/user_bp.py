from flask import Blueprint
from flask import Flask

user_bp = Blueprint("user_bp",__name__,url_prefix="/user")


app = Flask(__name__)


@app.route("/test")
def handle_test():
    return "HELLO FROM BLUEPRINT"



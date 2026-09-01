from flask import Flask

app = Flask(__name__)


@app.route("/")
def handle_home():
    return "HELLO THERE from main!"


if __name__ == "__main__":
    app.run(debug=True)

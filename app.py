from flask import Flask

app = Flask(__name__)


@app.route("/")
def homepage():
    return "<p>Hello, World! My Friend</p>"


if __name__ == "__main__":
    app.run(debug=True)

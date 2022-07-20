from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return "<p>Hello, World! My Friend</p>"


@app.route("/userinput")
def userinput():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

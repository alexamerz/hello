from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/greet", methods=["POST"])
def greet():
    first_name = request.form.get("first_name", "world")
    return render_template("greet_html", first_name = first_name)

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        name="이동훈",
        student_id="22011700"
    )


@app.route("/profile")
def profile():
    hobbies = ["게임하기", "영화 감상", "피아노 연주"]

    return render_template(
        "profile.html",
        hobbies=hobbies
    )


@app.route("/greet/<name>")
def greet(name):
    return render_template(
        "greet.html",
        name=name
    )
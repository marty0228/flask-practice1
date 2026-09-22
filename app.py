from flask import Flask, render_template
app = Flask(__name__)
@app.route("/hi/<name>")
def hi_template_render(name1):
    return render_template("hi.html", name=name1)
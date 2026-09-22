from flask import Flask, render_template
app = Flask(__name__)
@app.route("/hi/<name1>")
def hi_template_render(name1):
    return render_template("hi.html", name=name1)

app.run(debug=True)
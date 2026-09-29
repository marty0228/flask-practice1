from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return 'Index Page'
@app.route('/hello')
def hello():
    return 'Hello, World'
@app.route('/about')
def about():
    return 'About Us'
app.run(debug=True)
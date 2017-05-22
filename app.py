import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html')

@app.route('/environment')
def environment():
    return render_template(
        'environment.html',
        topic = 'environment'
    )

@app.route('/equality')
def equality():
    return render_template(
        'equality.html',
        topic = 'equality'
    )

@app.route('/education')
def education():
    return render_template(
        'education.html',
        topic = 'education'
    )

@app.route('/feminism')
def feminism():
    return render_template(
        'feminism.html',
        topic = 'feminism'
    )

@app.route('/science')
def science():
    return render_template(
        'science.html',
        topic = 'science'
    )
app.run(host = os.getenv('IP','0.0.0.0'), port = int(os.getenv('PORT',8080)))


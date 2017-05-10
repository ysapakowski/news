import os
from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
    r = requests.get(app.config['URL'] + app.config['API_KEY'])
    return render_template(
        'index.html',
        articles=json.loads(r.text)['articles'])



app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))


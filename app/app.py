from flask import Flask
import logging


app = Flask(__name__)
app.config.from_object('config.flask_config')

@app.route("/")
def hello():
    return "Hello World!"
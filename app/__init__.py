#!/usr/bin/python3

from flask import Flask, render_template
from app.home import home
from app.stack import stack
from app.about import about

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

app.register_blueprint(home)
app.register_blueprint(stack)
app.register_blueprint(about)

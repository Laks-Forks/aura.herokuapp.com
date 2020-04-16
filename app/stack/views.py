from . import stack
from flask import render_template

@stack.route('/stack')
def stackpage():
    return render_template('stack.html')
from app import app
from flask import render_template, send_file
from flask_security import login_required


@app.route('/')
@login_required
def index():
    return render_template('index.html')



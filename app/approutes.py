import os
from app import app 
from app.appmodels import Countries
from flask import render_template, jsonify, send_from_directory

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.png', mimetype='image/png')

@app.route("/")
def index():
    countries = Countries.query.order_by(Countries.name)
    return render_template('index.html',countries=countries)

@app.errorhandler(404)
def page_not_found_err(err):
    return render_template('notfound.html')

@app.errorhandler(Exception)
def unhandled_exception(e):
    return render_template('err.html',e=e)
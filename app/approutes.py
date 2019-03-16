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

@app.route('/searchcountries/<searchstring>')
def searchcountries(searchstring):        
    """
    Ajax route for search filter
    """    
    try:
        countries = Countries.query.order_by(Countries.name)               
        matcheditems = []   
        for item in countries:
            if (item.name.lower().find(searchstring.lower()) != -1 or item.name_official.lower().find(searchstring.lower()) != -1):                
                matcheditems.append(item.id)    
        resp = jsonify(matcheditems)
        resp.status_code=200
        return resp
    except Exception as e:
        raise Exception (str(e)) 

@app.route('/countrydetails/<id>')
def countrydetails(id):
    try:        
        country = Countries.query.filter(Countries.id==id)        
        if country.count()==0:            
            raise Exception('Unknown Country!')        
        return render_template('countrysnapshot.html', country=country[0])
    except Exception as e:        
        raise Exception(str(e))

@app.errorhandler(404)
def page_not_found_err(err):
    return render_template('notfound.html'), 404

@app.errorhandler(Exception)
def unhandled_exception(e):    
    return render_template('err.html',e=e), 500

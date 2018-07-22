from flask import render_template,url_for,make_response,request
from app import app

from app.views import index
from app.views import testpage
from app.views import report
from app.views import cure

@app.route('/hello/<name>')
def hello(name):
    return "FKu %s" % name


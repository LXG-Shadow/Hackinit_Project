from app.views import *
from app.api import getrs

@app.route('/report',methods=["GET","POST"])
def report():
    return render_template("diagnosisReport.html",result = getrs())
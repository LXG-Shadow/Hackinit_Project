from app.views import *

@app.route('/testpage',methods=["GET","POST"])
def testpage():
    pic1 = url_for("static", filename="img/1.jpg")
    pic2 = url_for("static", filename="img/2.jpg")
    return render_template("testPage.html")
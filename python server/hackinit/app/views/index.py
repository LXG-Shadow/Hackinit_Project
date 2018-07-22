from app.views import *

@app.route('/')
def index():
    pic1 = url_for("static", filename="img/1.jpg")
    pic2 = url_for("static", filename="img/2.jpg")
    return render_template("mindCure_index.html",pic1 = pic1,pic2 = pic2)
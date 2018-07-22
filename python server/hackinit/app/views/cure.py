from app.views import *

@app.route('/cure',methods=["GET","POST"])
def cure():
    music1 = url_for("static", filename="music/Being with My Soul.mp3")
    music2 = url_for("static", filename="music/Mountain Spring.mp3")
    music3 = url_for("static", filename="music/Kissing the Earth.mp3")
    music4 = url_for("static", filename="music/Dance of Gossamer.mp3")
    pic1 = url_for("static", filename="img/timg.jpg")
    pic2 = url_for("static", filename="img/wimg.jpg")
    pic3 = url_for("static", filename="img/uimg.jpg")
    pic4 = url_for("static", filename="img/vimg.jpg")

    return render_template("magicCure.html",music1 = music1,music2 = music2,
                           music3 = music3, music4 = music4,
                           pic1 = pic1,pic2 = pic2, pic3 = pic3, pic4 = pic4)
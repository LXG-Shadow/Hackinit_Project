from app.api import *

@app.route("/api/upload/sleeptime",methods= ["GET","POST"])
def uploadsleeptime():
    try:
        sleeptime = int(request.values.get("slptime"))
        if sleeptime > 15:
            return newjson("1", {"quilty": "good"})
        if sleeptime > 5:
            return newjson("1", {"quilty": "medium"})
        else:
            return newjson("1", {"quilty": "low"})
    except:
        return newjson("-3")
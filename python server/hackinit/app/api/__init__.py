from app import app
from flask import jsonify,request,render_template,url_for,make_response

from app.myapp import destree

clf= destree.getclf()
#import app.api.sleeptime


codes = {"-1":"传入参数错误",
         "-2":"请求方式不支持",
         "-3":"服务器内部错误",
         "1":"获取成功",
         "2":"已加入个人档案"}

resultss = []

def adrs(x):
    resultss.append(x)

def getrs():
    return resultss[len(resultss)-1]


def newjson(code,data = ""):
    return jsonify({"code":code,"message":codes[code],"data":data})


import app.api.getres


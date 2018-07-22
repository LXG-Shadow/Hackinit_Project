from app.api import *

@app.route("/api/result",methods=["GET","POST"])
def getres():
    flist = ['sex', 'age', 'isnevous', 'ispanic', 'HR', 'LB', 'disg', 'HA', 'isinsomnia', 'ishypocho', 'isirritab', 'isfever']
    featureList = []
    rowDict = {}
    rowDict2 = {}
    for i in range(0, 12, 1):
        value = request.values.get(str(i + 1))
        print(value)
        if value == "a":
            rowDict[flist[i]] = "a"
            rowDict2[flist[i]] = "b"
        else:
            rowDict[flist[i]] = "b"
            rowDict2[flist[i]] = "a"
    featureList.append(rowDict)
    featureList.append(rowDict2)
    print(featureList)
    # Vetorize features
    from sklearn.feature_extraction import DictVectorizer
    vec = DictVectorizer()
    dummyX = vec.fit_transform(featureList).toarray()
    predictedY = clf.predict([dummyX[0]])
    print(predictedY[0])
    if predictedY[0] == 0:
        adrs(0)
    else:
        adrs(1)
    print(getrs())
    return newjson("2",{"result":"数据已存储到你的个人档案中"})
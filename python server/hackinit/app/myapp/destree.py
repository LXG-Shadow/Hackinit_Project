from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree
from sklearn import preprocessing
from sklearn.externals.six import StringIO

def getclf():
    # Read in the csv file and put features into list of dict and list of class label
    allElectronicsData = open(r'dataset3.csv', 'rt')
    reader = csv.reader(allElectronicsData)
    headers = next(reader)

    print(headers)

    featureList = []
    labelList = []

    for row in reader:
        labelList.append(row[len(row) - 1])
        rowDict = {}
        for i in range(1, len(row) - 1):
            rowDict[headers[i]] = row[i]
        featureList.append(rowDict)

    print(featureList)

    # Vetorize features
    vec = DictVectorizer()
    dummyX = vec.fit_transform(featureList).toarray()

    print("dummyX: " + str(dummyX))
    print(vec.get_feature_names())

    print("labelList: " + str(labelList))

    # vectorize class labels
    lb = preprocessing.LabelBinarizer()
    dummyY = lb.fit_transform(labelList)
    print("dummyY: " + str(dummyY))

    # Using decision tree for classification
    # clf = tree.DecisionTreeClassifier()
    clf = tree.DecisionTreeClassifier(criterion='entropy')
    clf = clf.fit(dummyX, dummyY)
    return clf




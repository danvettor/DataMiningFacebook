from sklearn.linear_model import SGDClassifier
import random
import file_reader as fr
import numpy as np 
import operator

samples = 10
sgds = []
X_train = []
Y_train = []
num_lines = 10

output = open('../output.csv','w')

X_train, Y_train = fr.get_train_parameters('../processed_train.csv',num_lines)
X_test = fr.get_test_parameters('../processed_test.csv',num_lines)

X_train = np.array(X_train, dtype=float)
X_test = np.array(X_test, dtype=float)
Y_train = np.array(Y_train, dtype=float)

# cria os 100 classificadores 
for i in range(0,10):
    sgds.append(SGDClassifier(loss="modified_huber", alpha=0.01, n_iter=200, fit_intercept=True))

for clf in sgds:
    # pegar 1000 elementos aleatorios e treinar o clf
    elem = []
    label = []
    indexA = -1
    indexB = -1
    for i in range(samples):
        indexA = random.randint(0,len(X_train)-1)
        while indexA==indexB:
            indexA = random.randint(0,len(X_train)-1)
        elem.append(X_train[indexA])
        label.append(Y_train[indexA])
        indexB = indexA
    clf.fit(elem,label) 

results = []
classes = []

for clf in sgds:
    results.append(clf.predict_proba(X_test).tolist())
    classes.append(clf.classes_)

map3 = []

for result in results:

    index = []
    index = np.argsort(np.array(result))
    map3.append([linha[-3:] for linha in index ])

newMap3 = []
for mapList in map3:
    l = []
    i=0
    for m in mapList:
        i+= 1
        if len(m)<3:
            dif = 3 - len(m)
            for j in range(dif):
                m = np.append(m,0)
        l.append(m)  
    newMap3.append(l)

voting = {}
for c in classes:
    for elem in c:
        voting[elem] = 0

output.write("row_id, place_id")
output.write("\n")
i = 0
for linha in range(len(newMap3)):
    output.write(str(i) + ",")
    for clf in range(len(sgds)):
        for elem in newMap3[clf][linha]:
            voting[classes[clf][elem]]+=1
    for j in range(3):
        biggest_prob = max(voting.keys(), key=(lambda k: voting[k]))
        output.write(str(int(biggest_prob))+" ")
        voting[biggest_prob] = 0
    output.write("\n")
    for j in voting:
        voting[j] = 0
    # output.write
    i+=1


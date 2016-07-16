from sklearn.linear_model import SGDClassifier
import random

samples = 5
sgds = []

X_train=[
	[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],
	[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]
	]
X_test=[
	[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],
	[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]
	]
Y_train=[1,0,1,1,0,1,0,1,0,1]

#cria os 100 classificadores 
for i in range(0,100):
	sgds.append(SGDClassifier(loss="hinge", alpha=0.01, n_iter=200, fit_intercept=True))

for clf in sgds:
	# pegar 1000 eleme1ntos aleatorios e treinar o clf
	elem = []
	label = []
	for i in range(1,samples):
		index = random.randint(1,len(X_train)-1)
		elem.append(X_train[index])
		label.append(Y_train[index])
	clf.fit(elem,label)

results = []
for clf in sgds:
	results.append(clf.fit(X_test).predict_proba())
from sklearn.linear_model import SGDClassifier

sgds = []

#cria os 100 classificadores 
for i in range(0,100):
	sgds.append(SGDClassifier(loss="hinge", alpha=0.01, n_iter=200, fit_intercept=True))
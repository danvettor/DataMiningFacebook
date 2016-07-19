from sklearn.linear_model import SGDClassifier
import random
import file_reader as fr
import numpy as np 


samples = 1000
sgds = []
X_train = []
Y_train = []

# fr.print_file('../processed_test.csv')

# fr.print_file('../processed_test.csv',10)
num_lines = 4
output = open('../output.csv','w')

# fr.print_file('../processed_train.csv', num_lines)
X_train, Y_train = fr.get_train_parameters('../processed_train.csv',num_lines)
X_test = fr.get_test_parameters('../processed_test.csv',num_lines)
# print("tamanho train: "+ str(len(X_train)))
# print("tamanho test: "+ str(len(X_test)))

X_train = np.array(X_train, dtype=float)
X_test = np.array(X_test, dtype=float)
Y_train = np.array(Y_train, dtype=float)
# X_train=[
#   [1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],
#   [1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]
#   ]
# X_test=[
#   [1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],
#   [1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]
#   ]
# Y_train=[1,0,1,1,0,1,0,1,0,1]

# cria os 100 classificadores 
for i in range(0,100):
    sgds.append(SGDClassifier(loss="modified_huber", alpha=0.01, n_iter=200, fit_intercept=True))

for clf in sgds:
    # pegar 1000 eleme1ntos aleatorios e treinar o clf
    elem = []
    label = []
    for i in range(1,samples):
        index = random.randint(0,len(X_train)-1)
        elem.append(X_train[index])
        label.append(Y_train[index])
    clf.fit(elem,label) 

results = []
for clf in sgds:
    results.append(clf.predict_proba(X_test))
    # print (clf.classes_)

classes = sgds[0].classes_


map3 = []
for result in results:
    # index = []

    index = np.argsort(np.array(result))
    map3 = [linha[len(linha)-3:len(linha)] for linha in index ]
print(map3)



# output.write("row_id, place_id")
# output.write("\n")
# _id = 0
# for mapIndex in map3:
# 	output.write(str(_id)+",")
# 	_id+=1
# 	for i in mapIndex:
# 		output.write(str(int(classes[i]))+" ")
# 	output.write("\n")
# print(map3[0])

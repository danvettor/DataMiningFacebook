from sklearn.linear_model import SGDClassifier
import random
import file_reader as fr
import numpy as np 


samples = 10
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
for i in range(0,4):
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
    results.append(clf.predict_proba(X_test).tolist())
    # print (clf.classes_)

classes = sgds[0].classes_


map3 = []
# print results
# exit(0)
for result in results:
    # print result
    # for example in result:
        # print example
    index = []

    index = np.argsort(np.array(result))
    map3.append([linha[-3:] for linha in index ])
    # map3 = [linha[len(linha)-3:len(linha)] for linha in index ]

print(map3[0][0])



# =========================
# TA DANDO MERDA AQUI
# =========================
for mapList in map3:
    print (mapList)
    i=0
    for m in mapList:
        i+= 1
        if len(m)<3:
            print("entrei na condicao")
            m = np.insert(m,-1,0)
            print(map3[i][:])
            print("novo array" + str(m))


voting = {}
for c in classes:
    voting[c] = 0
# print(voting)

# quantidade de linhas de teste
for i in range(len(map3)):
    # quantidade de classificadores
    for j in range(len(map3[0])):
        # pegando os 3 itens do array
        # print(classes[map3[i][j]])
            temp=map3[i][j][2]
        # for k in range(len(map3[0][0])):
            # voting[classes[map3[i][j][k]]]+=1 

# print(voting)
# print(max(voting))

print(map3)

# print(voting)
# output.write("row_id, place_id")
# output.write("\n")
# _id = 0
# for mapIndex in map3:
#   output.write(str(_id)+",")
#   _id+=1
#   for i in mapIndex:
#       output.write(str(int(classes[i]))+" ")
#   output.write("\n")
# print(map3[0])

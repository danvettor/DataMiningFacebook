import datetime
# print(
#         datetime.datetime.fromtimestamp(
#             int("1284101485")
#         ).strftime('%Y-%m-%d %H:%M:%S')
# )

def trainFilter():
    file = open('train.csv','r')

    i = 0
    X = []
    accuracy = []
    
    for line in file:

        if i == 0:
            pass
        else:
            vec = line.split('\n')
            vec.remove("")
            for string in vec:
                vec = string.split(',')
            data = vec[4]
            accuracy.append(int(vec[3]))
            day = int(datetime.datetime.fromtimestamp(int(data)).weekday())
            hour = int(datetime.datetime.fromtimestamp(int(data)).strftime('%H'))
            del vec[4]
            vec.append(day)
            vec.append(hour)
            X.append(vec)
            # del vec[0]
        i+=1
    file.close()
    maxAccuracy = max(accuracy)
    minAccuracy = min(accuracy)
  
    for j in X:
        j[3] = (float(j[3])-float(minAccuracy))/float((maxAccuracy - minAccuracy))

    file = open('cleanTrain.csv','w')
    file.write("row_id, x, y, acuraccy,place_id, day, hour")
    file.write("\n")
    for line in X:
        for element in line:
            file.write(str(element)+",")
        file.write("\n")


trainFilter()
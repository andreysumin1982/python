# Привести массив к такому виду [[1,2], [4,5], [7,8,9]...]
dataset = [1,2,4,5,7,8,9,10,14,15,16,18,19,20,28,33,34]
#
def f1(outputData):
    tempset = [[]]
    prew_item ,next_item = 0, 0
    for item in outputData:
        if (next_item + 1) == item:
            tempset[prew_item].append(item)
            next_item = item
        else:
            tempset.append([item])
            prew_item +=1
            next_item = item
    return tempset
#
for item in f1(dataset):
    print(item, item[0], item[-1])

#
if __name__ == '__main__':
    pass

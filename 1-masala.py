import os; os.system("cls")

def takror(mylist):
    mydct = {}
    son = set()

    for i in mylist:
        if i not in son:
            mydct[i] = mylist.count(i)
            son.add(i)
    return mydct

mylist = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]
yig = takror(mylist)
print(yig)
x = 15
y = 3

z = "this is a string"

a = "hello"
b = "world"
c = "again"

myList = [1, 12, 3, 45, 5]

def myPrint(words):
    print(words,"ok.")

def myFunction(start, vList, step):
    for i in range(start, len(vList), step):
        print(vList[i])

def myRecursiveFunction(vList):
    if len(vList) > 0:
        print(vList ,pop())
        myRecursiveFunction(vList)

myFunction(["hello", 1, True, 3.14159], 2)
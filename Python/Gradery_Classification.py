#Written in Python 2.7
#By: Hossein Dehghanipour

import random

def readFromFile(fileName):
    f = open(fileName + ".txt" , "r")
    x = f.read().split('\n')
    while "" in x : x.remove("")
    f.close()
    return x
def randomizeStudents(totalStd , arrayList , amount ):
    counter = 0
    index = 0
    for i in range(0,amount):
        randIndex = random.randint(0 , len(totalStd)-1 )
        student = totalStd.pop(randIndex)
        arrayList.append(student)
    return arrayList
    
def writeToFile(fileName , my_list):
    f = open(fileName + ".txt" , "w+")
    for item in my_list:
        f.write("%s\n" % item)
    f.close()
#Main Function
def Classify(fileName):
	class1 = []
	class2 = []
	x = readFromFile(fileName)
	class1 = randomizeStudents(x,class1,len(x)/2)
	class2 = randomizeStudents(x,class2,len(x))
	writeToFile("classOne" , class1)
	writeToFile("classtwo" , class2)
	print "Class One : " , class1
	print "Class 2 : " , class2
	
	




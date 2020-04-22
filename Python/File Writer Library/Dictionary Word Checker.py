# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:47:13 2020

@aut
hor: Hossein
"""
from os import system
wordFilename = "words.txt"
password = 123


def addToFile(word,fileName):
    try:
        f = open(fileName, "a")
        f.write(str(word) + "\n")
        f.close()
    except:
        print("File Not Found")

def createFile(fileName):
    f = open(fileName , "w+")
    f.close()

def readFile(fileName):
    try:
        f = open(fileName,"r")
        publicWords = f.read().split('\n')
        f.close()
        return publicWords,True

    except:
        return [],False

def test():
    for i in range (100,200):
        addToFile(i,wordFilename)

def wordExists(word):
    wordsList,foundTheFile = readFile(wordFilename)
    if(foundTheFile == True):
        if str(word) in wordsList :
            return True
        return False
    createFile(wordFilename)
    return False

def getLen():
    wordsList,foundTheFile = readFile(wordFilename)
    return len(wordsList)

def backup(fromFilename):
    fileParts = fromFilename.split(".")
    backupFileName = str(fileParts[0]) + "-BackUp." + str(fileParts[1])
    createFile(backupFileName)
    arrList,status = readFile(fromFilename)
    for item in arrList :
        addToFile(item,backupFileName)
    print("Backup File Created")

def fileToArray(fileName):
    arr,stat = readFile(fileName)
    return arr

def arrayToFile(arr , fileName):
    createFile(fileName)
    for item in arr :
        addToFile(item,fileName)

def delete(indexNo,fileName):
        lines = fileToArray(fileName)
        del lines[indexNo]
        arrayToFile(lines, fileName)


def start():

    while True :
        i = getLen() + 1
        print(str(i) + ": ")
        word = input()
        # ====================================
        try :
            #it's a Number
            word + 1
            delete(word-1,wordFilename)
            system('cls')
            continue
        except :    
            # ====================================
            if(word == "q"):
                break
            # ====================================
            elif(word == "p"):
                listOfWords,status = readFile(wordFilename)
                print("\n=====================================================\n")
                print(str(listOfWords) + "\n")
                print("\n=====================================================\n")
            # ====================================
            elif (word == "b"):
                enteredPass = input("Password To get Backup : ")
                if ( enteredPass == str(password) ):
                    backup(wordFilename)
            # ====================================
            elif(word =="c"):
                enteredPass = input("Password To Delete Everything : ")
                if ( enteredPass == str(password) ):
                    createFile(wordFilename)

            # ====================================
            else:
                if(wordExists(word) == False):
                    addToFile(word,wordFilename)
                else:
                    print("Word Already Added")
    print("Done")
    input()


start()

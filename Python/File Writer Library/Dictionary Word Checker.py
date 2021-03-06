# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:47:13 2020

@aut
hor: Hossein
"""
from Writer import Writer


wordFilename = "words.txt"
password = 123

def testRedundancyRemover():
    writer = Writer("test2.txt")
    writer.removeRedundantData()

def start():
    writer = Writer(wordFilename)
    while True :
        i = writer.getLen() + 1
        print(str(i) + ": ")
        word = input()
        filter(lambda a: a != "\n", word)
        # ====================================
        if(word[0] == "$"):
            word = word.split(" ")[1:]
            filter(lambda a: a != " ", word)
            writer.deleteContent(word)
            
        # ====================================
        elif(word == "q"):
            break
        # ====================================
        elif(word == "p"):
            listOfWords = writer.readFile()
            print("\n=====================================================\n")
            print(str(listOfWords) + "\n")
            print("\n=====================================================\n")
        # ====================================
        elif (word == "b"):
            enteredPass = input("Password To get Backup : ")
            if ( enteredPass == str(password) ):
                writer.createBackup()
        # ====================================
        elif(word =="c"):
            enteredPass = input("Password To Delete Everything : ")
            if ( enteredPass == str(password) ):
                writer.clearFile()

        # ====================================
        else:
            if( writer.appendNoneRepeated(word) == False):
                print("Word Already Added")
    print("Done")
    input()


start()
#testRedundancyRemover()

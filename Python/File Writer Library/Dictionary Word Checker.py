# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:47:13 2020

@aut
hor: Hossein
"""
from Writer import Writer
from os import system
wordFilename = "words.txt"
password = 123



def start():
    writer = Writer(wordFilename)
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

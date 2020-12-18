# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 21:06:44 2020

@author: Hossein
"""

import string
import random

lowerCase = list(string.ascii_lowercase)
upperCase = list(string.ascii_uppercase)
miscList = ['{','}','$','#','@','!','-','_','+','=','(',')','&','%',]
numbersList = list(string.digits)



def passwordGenerator(passwordLen, fullList):
    password = ""
    counter = 0 
    while( counter < passwordLen ):
        index = random.randint(0,len(fullList)-1)
        password += fullList[index]
        counter += 1
    return password

def main():
    
    carryOn = "Y"
    while(carryOn == "Y" or carryOn == "y"):
        fullList = []
        # LowerCase
        print("Include Lower Case Alphabets? (Y/N) ")
        lowerCaseOption = input()
        if(lowerCaseOption == "Y" or lowerCaseOption == "y"):
           fullList += lowerCase 
        
        #UpperCase
        print("Include Upper Case Alphabets? (Y/N) ")
        upperCaseOption = input()
        if(upperCaseOption == "Y" or upperCaseOption == "y"):
            fullList += upperCase
                    
        # MiscAlphabets
        print("Include Miscellaneous Alphabets like [- , @ ]? (Y/N) ")
        miscOption = input()
        if(miscOption == "Y" or miscOption == "y"):
            fullList += miscList
            
        #Numbers    
        print("Include Numbers ? (Y/N) ")
        numbersOption = input()
        if(numbersOption == "Y" or numbersOption == "y"):
            fullList += numbersList
        
        
        lengthOfPass = input("Length of the Password ?")
        x = passwordGenerator(int(lengthOfPass),fullList)
        print( x )
        
        carryOn = input("Continue ? (Y/N)")
        

main()

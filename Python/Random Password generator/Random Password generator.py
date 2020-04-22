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

fullList = lowerCase + miscList + upperCase +numbersList 

def passwordGenerator(passwordLen):
    password = ""
    counter = 0 
    while( counter < passwordLen ):
        index = random.randint(0,len(fullList)-1)
        password += fullList[index]
        counter += 1
    return password

def main():
    x = passwordGenerator(32)
    print( x )

main()

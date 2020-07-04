# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 04:27:41 2020

@author: Hossein
"""
import string 
from string import punctuation



class CommandCenter :
    MaxLength = 12
    MinLenght = 11

def printCombination(arr, n, r):
    results = []
    data = [0]*r
    combinationUtil(arr, data, 0,n - 1, 0, r,results)
    return results
                 
def listToString(s):   
    str1 = ""   
    for ele in s:  
        str1 += str(ele)    
    return str1  

def combinationUtil(arr, data, start,end, index, r ,  results):
    if(index == r):
        string = listToString(data)
        results.append(string)
        return
    
    i = start
    while( i <= end and end -i + 1 >= r - index ):
        data[index] = arr[i]
        combinationUtil(arr, data, i + 1,end, index + 1, r , results)
        i+= 1
  

# Create the Array List :
def createReferenceArray():
    punct = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`','~']
    alhpabets = list(string.ascii_letters) 
    numeric = [1,2,3,4,5,6,7,8,9,0]
    arr = numeric + alhpabets + punct
    #print(list(punctuation))
    return arr
    
def obtainCombination(referenceArray):
    n = len(referenceArray);
    results = []
    for r in range(CommandCenter.MinLenght , CommandCenter.MaxLength ): 
        results = printCombination(referenceArray, n, r); 
    return  results
     
    

def main():
    arr = createReferenceArray() 
    print("Reference Length : " + str(len(arr)))
    
    results = obtainCombination(arr) 
    print("Results Len : " + str(len(results)))
    
   
    print("Done!")
 
main()
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 14:03:05 2020

@author: Hossein
"""
from Writer import *


def tuplize(lines):
    tupleForm = (0,0)
    tuples = []
    for line in lines:
        eachLine = line.split(" ")
        tupleForm = ( float(eachLine[0]),  float(eachLine[1])  )
        tuples.append(tupleForm)
    return tuples


def removeX(lists):
    return filter(lambda a: a != "X", lists)

def Calucalte(type1):
    fileOperator = Writer("Scores.txt")
    scores = fileOperator.readFile()
    scores = removeX(scores)
    ScoresTuples = tuplize(scores)
    
    
    
  
    scoresSummation = 0 
    unitsSummation = 0
    
    for scoresTuple in ScoresTuples:
        score = scoresTuple[0] * 5
        unit = scoresTuple[1]
        
        
        GPA = 0 
        if (type1 == True):
            if (score >= 0  and  score < 60):
                GPA = 0
            elif (score >= 60  and  score < 67):
                GPA = 1
            elif (score >= 67  and  score <= 69):
                GPA = 1.3
            elif (score >= 70  and  score < 73):
                GPA = 1.7
            elif (score >= 73  and  score < 77):
                GPA = 2
            elif (score >= 77  and  score < 80):
                GPA = 2.3
            elif (score >= 80  and  score < 84):
                GPA = 2.7
            elif (score >= 84  and  score < 87):
                GPA = 3
            elif (score >= 87  and  score < 90):
                GPA = 3.3
            elif (score >= 90  and  score < 94):
                GPA = 3.7
            elif (score >= 94  and  score <= 100):
                GPA = 4.0

            
        print("Normal: " + str(scoresTuple[0]) + "  |Score : " + str(score) + "  | Unit : " + str(unit) + " | GPA: " + str(GPA))
        scoresSummation += GPA * unit
        unitsSummation += unit
        
    return  scoresSummation/unitsSummation 
            
GPA = Calucalte(True)
print(GPA)
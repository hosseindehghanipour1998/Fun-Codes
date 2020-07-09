# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 04:27:41 2020

@author: Hossein
"""
import string 
from string import punctuation
from ExternalLibraries.Writer import Writer as Writer



# Global Arrays
PUNCTUATIONS_ARRAY = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`','~']
ALPHABETS_ARRAY = list(string.ascii_letters) 
NUMERIC_ARRAY = [1,2,3,4,5,6,7,8,9,0]


class CommandCenter :
    MinLenght = 4
    MaxLength = 6
    CONTROLLER = 0
    COUNTER = 0 
    TERMINATE = False
    FILE_NAME  = "x.rar"
    

def calculateCombination(arr, r):
    results = []
    data = [0]*r
    n = len(arr)
    combinationUtil(arr, data, 0, n - 1, 0, r,results)
    return results 
                 
def listToString(s):   
    str1 = ""   
    for ele in s:  
        str1 += str(ele)    
    return str1  

def combinationUtil(arr, data, start , end, index, r ,  results):
    if(index == r):
        string = listToString(data)
        breakWithWord(string)
        return
    
    i = start
    while( i <= end and end -i + 1 >= r - index ):
        data[index] = arr[i]
        combinationUtil(arr, data, i + 1,end, index + 1, r , results)
        i+= 1
  

# Create the Array List :
def createReferenceArray():
    arr = ALPHABETS_ARRAY + NUMERIC_ARRAY + PUNCTUATIONS_ARRAY
    return arr
  
def duplicateCombinationUtil (arrayReference ,  lenght  ):
  CommandCenter.CONTROLLER += 1
  if lenght < 1:
    return [[]]
  subtable = duplicateCombinationUtil( arrayReference , lenght-1)
  l = []
  for i  in range (0,len(subtable)) :
      for j in range(0,len(arrayReference)):
          x = "".join(subtable[i])
          try:
              y = "".join(arrayReference[j])
          except:
               y = arrayReference[j]
          
          key = str(str(x) + "" + str(y))
          if(CommandCenter.CONTROLLER == lenght+1  and CommandCenter.TERMINATE == False):
              CommandCenter.COUNTER += 1
              # @key is the passcode combination created at each step
              # if you want to ignore adding it to an array, use it here
              breakWithWord(key)
          elif (CommandCenter.TERMINATE == True):
              return 

          else :
              l.append(z)
  return l
  #return [ row + [v] for row in subtable for v in arrayReference ]



def duplicateCombination( arrayReference ,  lenght  ):
    arr = duplicateCombinationUtil(arrayReference,lenght)
    return arr
 
    
# creates combinations from MinLength to MaxLength size
def obtainCombination(referenceArray , withDuplicate = False ):
    results = []
    for length in range(CommandCenter.MinLenght , CommandCenter.MaxLength ): 
        if(withDuplicate == False):
            results = calculateCombination(referenceArray,length); 
        elif (withDuplicate == True ):
            results = duplicateCombination (referenceArray ,length)
    return  results
     
def calucltePossibleResutls(referenceArray) :
    n = len(referenceArray);
    summation = 0 
    for r in range(CommandCenter.MinLenght , CommandCenter.MaxLength ): 
        summation += n ** r
        print(str(n) + " ^ " + str(r) + " = " + str(summation) )
    return summation
 
    
# tries the zip/rar file with an array of words
def breakTheCode(results):
    
     # decryption for zip file
    '''
    from zipfile import ZipFile

    zip_file = 'x.rar'
    password = '123'

    with ZipFile(zip_file) as zf:
        zf.extractall(pwd=bytes(password,'utf-8'))       
        '''
    # decryption for rar file
    from ExternalLibraries.Writer import rarfile as rarfile
    r = rarfile.RarFile(CommandCenter.FILE_NAME)
    for item in results :   
        try :
            r.extractall(pwd=item)
            print("Password is : " + item)
        except:
            continue;
    r.close()
    
    
# tries the rar file with a word   
def breakWithWord(word):
    import rarfile
    r = rarfile.RarFile(CommandCenter.FILE_NAME)
    try:
        r.extractall(pwd=word)
        print("Password is : " + word)
        CommandCenter.TERMINATE = True
        return

    except:
        2==2 # do nothing
    r.close()


def main():

    arr = createReferenceArray() 
    print("Reference Length : " + str(len(NUMERIC_ARRAY)))
    
    possibleNumberOfOutputs = calucltePossibleResutls(NUMERIC_ARRAY)
    print("Possible Number Of Outputs : "  + str(possibleNumberOfOutputs))
    
    print("Processing ... Please Wait :D ")
    
    results = obtainCombination(NUMERIC_ARRAY ,  True) 
    #print("Results Len : " + str(len(results)))
    #print(results)
    

    #breakTheCode(results)
    
    # Writes the results in a file
    '''
    fileWriter = Writer("test.txt")
    fileWriter.clearFile()
    fileWriter.arrayToFile(results)
    '''
    print("Done!")
 
main()

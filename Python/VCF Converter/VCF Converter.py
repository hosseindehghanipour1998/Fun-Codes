

def openAndReturnContents(fileName):
    fileFullName = fileName + ".vcf"
    fileObject = open(fileFullName,"r")
    content = fileObject.read().split("BEGIN:VCARD")
    fileObject.close()
    return content    

def convertData(rawContentArray):
    processedContacts = []
    i = 0 
    
    for contact in rawContentArray:
        details = contact.split('\n')
        print(str(i) +"-" + str(details) )
        try:     
            nameList = details[3]
            tel =  details[4]
            nameTelTuple = ( nameList , tel)
            processedContacts.append(nameTelTuple)
            i += 1     
        except:   
            print("Invalid format for Contact")
    return processedContacts


def writeToFile(fileName,arrayList):
    fileFullName = fileName + ".txt"
    fileObject = open(fileFullName,"w")
    print(arrayList)
    for item in arrayList:
        print(item)
        fileObject.write("Name: " + item[0] +'\n')
        fileObject.write("Phone: " + item[1] +'\n')
        fileObject.write("==================== \n")

def run():
    # C:\Users\hosse\Desktop 
    fileName ="C:\\Users\\hosse\\Desktop\\Contacts"
    content = openAndReturnContents(fileName)
    processedData = convertData(content)
    writeToFile("ContactInTextFile" ,processedData )
    
run()
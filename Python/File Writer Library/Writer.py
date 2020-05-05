class Writer :


    def __init__(self,filePath):
        self.filePath = filePath
        if ( self.fileExists() == True):
            print("Handle Binded With Existing File Named : " + str(self.filePath))
        else :
            self.createFile()
            print("New File Named " + str(self.filePath) + " Created !")



    def append(self,string):
        try:
            f = open(self.filePath, "a")
            f.write(str(string) + "\n")
            f.close()
        except:
            print("File Not Found")


    def createFile(self):
        f = open(self.filePath, "w+")
        f.close()



    def readFile(self):
        try:
            f = open(self.filePath,"r")
            lines = f.read().split('\n')
            f.close()
            return lines
        except:
            return None



    def fileExists(self):
        try:
            f = open(self.filePath,"r")
            f.close()
            return True

        except:
            return False



    def __constentExists(self,content):
        wordsList = readFile(self.filePath)
        if(wordsList != None):
            if str(content) in wordsList :
                return True
            return False
        createFile(self.filePath)
        return False



    def arrayToFile(self,arr):
        if(fileExists(self.filePath) == False ):
            createFile(self.filePath)
        for item in arr :
            append(item,self.filePath)


    def getLen():
        wordsList = readFile(self.filePath)
        if(wordsList != None):
            return len(wordsList)
        return None



    def createBackup(self):
        fileParts = self.filePath.split(".")
        backupFileName = str(fileParts[0]) + "-BackUp." + str(fileParts[1])
        createFile(backupFileName)
        arrList,status = readFile(self.filePath)
        for item in arrList :
            addToFile(item,backupFileName)
        print("Backup File Created")



    def appendNoneRepeated(self,content):
        if (__constentExists(content) != False ):
            append(content)
            return True # Successful Operation
        else :
            return False # Word Already Exists



    def deleteContent(self,contentList):
        lines = self.readFile()
        for line in lines :
            for item in contentList:
                lines.replace(item, "")
        self.createFile()
        for item in lines :
            self.append(item)

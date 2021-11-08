import random

class FileListGenerator:

    filelist = []
    folderlist = []

    def __init__(self, numberFiles, numberFolders, folderDepth, folderPrefix):
        fileObj = open("suffix.csv", "r") #opens the file in read mode
        suffix = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        fileObj = open("subjects.csv", "r") #opens the file in read mode
        subjects = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        fileObj = open("subjects2.csv", "r") #opens the file in read mode
        subjects2 = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        fileObj = open("directories.csv", "r") #opens the file in read mode
        directories = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()


        for i in range(0,numberFiles):
            # create filename
            extension = random.choice(suffix)
            filename = ""
            if random.random() > 0.5: # 50% chance of being a two word file name 
                filename = random.choice(subjects) + random.choice(subjects2) + extension
            else:
                filename = random.choice(subjects) + extension

            self.filelist.append(filename)

        for i in range(0,numberFolders):
            # how deep will the folder structure go
            depths = int(random.random() * folderDepth)
            folder = folderPrefix
            for j in range(0,depths):
                folder = folder + random.choice(directories) + "/"
            self.folderlist.append(folder)


    def getFullFile(self):
        file = random.choice(self.filelist)
        folder = random.choice(self.folderlist)
        return folder + file

    def getFile(self):
        file = random.choice(self.filelist)
        return file

    def getFolder(self):
        folder = random.choice(self.folderlist)
        return folder
      
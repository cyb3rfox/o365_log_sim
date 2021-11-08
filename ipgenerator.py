

import random

class IPGenerator:

    iplist = [] 

    def __init__(self):
        fileObj = open("ips.csv", "r") #opens the file in read mode
        self.iplist = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()

    def getIP(self):
        return self.iplist[random.randint(0, len(self.iplist)-1)]
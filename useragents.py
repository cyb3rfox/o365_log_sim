import random

class UserAgent:

    useragents = []

    def __init__(self):
        fileObj = open("useragents.csv", "r") #opens the file in read mode
        self.useragents = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()

    def getUserAgent(self):
        return random.choice(self.useragents)
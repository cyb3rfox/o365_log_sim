from simulateduser import SimulatedUser
import random



class UserGenerator:

    def generate_users(self, domain, count, ipgenerator, filelistgenerator, useragents):
        # find name in firstname list
        fileObj = open("firstnames.csv", "r") #opens the file in read mode
        firstnames = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        
        # find name in lastname list
        fileObj = open("surnames.csv", "r") #opens the file in read mode
        lastnames = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()

        # fake uid
        uid = "sdsdfsdfsdfsdfsdfsdf"

        #generate user object

        users = []
        for i in range(0, count):
            firstname_index = random.random()*len(firstnames)
            lastname_index = random.random()*len(lastnames)
            firstname = firstnames[int(firstname_index)].lower()
            lastname = lastnames[int(lastname_index)].lower()
            email = firstname + "." + lastname +  "@" + domain
            user = SimulatedUser(username=email, user_id=uid, currently_loggedon=False,current_ip=ipgenerator.getIP(),activeness=random.random(), filelistgenerator = filelistgenerator, ipgenerator=ipgenerator, useragents=useragents)
            users.append(user)


        return users
          
    


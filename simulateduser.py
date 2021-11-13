import random

class SimulatedUser:
    

    def __init__(self, username, user_id, currently_loggedon, current_ip, activeness, filelistgenerator, ipgenerator, useragents):
        self.username = username
        self.user_id = user_id
        self.currently_loggedon = currently_loggedon
        self.current_ip = current_ip
        self.activeness = activeness  # should be between 0 and 1
        self.filelistgenerator = filelistgenerator
        self.ipgenerator = ipgenerator
        self.useragents = useragents
        self.useragent = useragents.getUserAgent()


    def create_logs(self,time):
        # is that user active in that timeframe?

        # is there an action in this second
        rand = random.random() * 100  
        # maximum 8% chance of activation every second for an active user. 
        # Results in an average of 4.8 actions per minute
        activation_threshold = 2 * self.activeness 
        if  activation_threshold <= rand: 
            return None # not action second

        # let's see if the user needs a new ip. maybe every 500 calls in avarage?

        if(random.randint(0,500) == 0):
            self.ip = self.ipgenerator.getIP()

        # what action is it?
        # if user is not yet logged in, it will be a logon action
        if not self.currently_loggedon:
            return self.action_logon(time)

        # user is logged on already, there could still be another logon or any other action
        
        return self.pick_action(time)



    def pick_action(self, time):

        actions = [
            {"action": self.action_logon, "occurance": 247},
            {"action": self.action_file_accessed, "occurance": 11633},
            {"action": self.action_update_device, "occurance": 354},
            {"action": self.action_file_previewed, "occurance": 265},
            {"action": self.action_file_modified_extended, "occurance": 195},
            {"action": self.action_update_user, "occurance": 40},
            ]

        # 2 calculate probability in % for each action
        action_sum = 0
        for action in actions:
            action_sum = action_sum + action["occurance"]
        
        probabilities = []
        for action in actions:
            probabilities.append(action["occurance"] / action_sum)


        # 4 random number hits a hitband
        selected_action = (random.choices(actions, weights=probabilities,k=1))[0]
        return selected_action["action"](time)

  

##################################
#        Actions below           #
##################################

    
    def action_logon(self,time):
        self.currently_loggedon = True
        result = "{}Z,{},{},{},{},{}"


        return result.format(time.isoformat(), self.current_ip , self.username, "User logged in", "",self.useragent) # useragent

    def action_file_accessed(self,time):
        result = "{}Z,{},{},{},{},{}"
        return result.format(time.isoformat(), self.current_ip , self.username, "FileAccessed", self.filelistgenerator.getFullFile(),self.useragent)

    def action_update_device(self,time):
        result = "{}Z,{},{},{},{},{}"
        return result.format(time.isoformat(), self.current_ip , self.username, "Update device.", "",self.useragent)

    def action_file_previewed(self,time):
        result = "{}Z,{},{},{},{},{}"
        return result.format(time.isoformat(), self.current_ip , self.username, "FilePreviewed", self.filelistgenerator.getFullFile(),self.useragent)

    def action_file_modified_extended(self,time):
        result = "{}Z,{},{},{},{},{}"
        return result.format(time.isoformat(), self.current_ip , self.username, "FileModifiedExtended", self.filelistgenerator.getFullFile(),self.useragent)

    def action_update_user(self,time):
        result = "{}Z,{},{},{},{},{}"
        return result.format(time.isoformat(), self.current_ip , self.username, "Update user.", "",self.useragent) # what was updated?

    

    
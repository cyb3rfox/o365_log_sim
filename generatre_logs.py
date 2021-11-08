
from simulateduser import SimulatedUser
from usergenerator import UserGenerator
from ipgenerator import IPGenerator
from filelistgenerator import FileListGenerator
from useragents import UserAgent
import datetime



def generate(start_time,end_time,user_count):
    
    ipgenerator = IPGenerator()
    filelistgenerator = FileListGenerator(100,100,3,"https://srl.sharepoint.com/Documents/")
    useragents = UserAgent()
    users = UserGenerator().generate_users("srl.com",user_count,ipgenerator,filelistgenerator, useragents)


    current_time = start_time

    while(current_time < end_time):
        current_time = current_time + datetime.timedelta(seconds=1)
        for user in users:
            log = user.create_logs(current_time)
            if(log):
                print(log)
    


start = datetime.datetime(2021,1,1,11,34,59)
end = datetime.datetime(2021,1,1,17,35,59)
generate(start,end,50)



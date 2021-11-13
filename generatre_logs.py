
from simulateduser import SimulatedUser
from usergenerator import UserGenerator
from ipgenerator import IPGenerator
from filelistgenerator import FileListGenerator
from useragents import UserAgent
import datetimerm 



def generate(start_time,end_time,user_count):
    
    ipgenerator = IPGenerator()
    filelistgenerator = FileListGenerator(100,100,3,"https://starkresearchlabs.sharepoint.com/Documents/")
    useragents = UserAgent()
    users = UserGenerator().generate_users("starkresearchlabs.com",user_count,ipgenerator,filelistgenerator, useragents)

    tdungan = SimulatedUser("timothy.dungan@starkresearchlabs.com","",False,"50.211.194.23", 0.8,filelistgenerator,ipgenerator,useragents)
    nromanoff = SimulatedUser("natashe.romanoff@starkresearchlabs.com","",False,"50.211.197.156", 0.5,filelistgenerator,ipgenerator,useragents)

    users.append(tdungan)
    users.append(nromanoff)

    current_time = start_time

    while(current_time < end_time):
        current_time = current_time + datetime.timedelta(seconds=1)
        for user in users:
            log = user.create_logs(current_time)
            if(log):
                print(log)
    


start = datetime.datetime(2020,1,20,12,00,00)
end = datetime.datetime(2020,1,22,17,35,12)
generate(start,end,80)



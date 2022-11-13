 
import os

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

file = 'liquidweb.txt'
#os.system('cat '+ file+" | httpx > http_"+file)
temp = open("http_"+file,'r').read().splitlines()

for line in temp:
    #print(line)
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        newline = line +"/cdn-cgi/image/width/https://raw.githubusercontent.com/j1t3sh/test/main/Spectrocoin.png"
        response = requests.get(newline, verify=False)
        if response.status_code==200 or response.status_code==204 or response.status_code==301 or response.status_code==302:
            print(str(newline) + " - " + str(response.status_code))
    except:
        continue
        # if response.status_code==200:
        #     print("hello")        


# Making a get request


# print request status_code


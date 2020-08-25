# importing the requests library 
import requests 
import random


import random
# print(random.randint(1,101))

rand = random.randint(1,101)
print(rand)

randNum = str(rand)
# sending post request and saving response as response object 
r = requests.post("https://api.telegram.org/bot1238646884:AAGUYD9VFsGQ8cF5BqRJWP_qxWIF43sA8kw/sendMessage?chat_id=-1001247118458&text=Today " + randNum + "% of the land has been developed") 

if rand < 40 :
    r = requests.post("https://api.telegram.org/bot1238646884:AAGUYD9VFsGQ8cF5BqRJWP_qxWIF43sA8kw/sendMessage?chat_id=-1001247118458&text=Theres a chance!") 
    # print("Less than 40")

if rand > 41 and rand < 60 :
    r = requests.post("https://api.telegram.org/bot1238646884:AAGUYD9VFsGQ8cF5BqRJWP_qxWIF43sA8kw/sendMessage?chat_id=-1001247118458&text=It might happen, but not likley") 
    # print("Less than 60")
if rand > 61 :
    r = requests.post("https://api.telegram.org/bot1238646884:AAGUYD9VFsGQ8cF5BqRJWP_qxWIF43sA8kw/sendMessage?chat_id=-1001247118458&text=Its not happening today...") 
    # print("Over 60")
# extracting response text 
# response = r.text 
# print(response) 


# TESTING ----------------------------------------------------------------------------------- TESTGROUP

# # importing the requests library 
# import requests 
# import random


# import random
# # print(random.randint(1,101))

# rand = random.randint(1,101)
# print(rand)

# randNum = str(rand)
# # sending post request and saving response as response object 
# r = requests.post("https://api.telegram.org/bot1238646884:AAGUYD9VFsGQ8cF5BqRJWP_qxWIF43sA8kw/sendMessage?chat_id=-1001247118458&text=Today " + randNum + "% of the land has been developed") 

# if rand < 40 :
#     r = requests.post("https://api.telegram.org/bot1238646884:AAGUYD9VFsGQ8cF5BqRJWP_qxWIF43sA8kw/sendMessage?chat_id=-1001247118458&text=Theres a chance!") 
#     # print("Less than 40")

# if rand > 41 and rand < 60 :
#     r = requests.post("https://api.telegram.org/bot1238646884:AAGUYD9VFsGQ8cF5BqRJWP_qxWIF43sA8kw/sendMessage?chat_id=-1001247118458&text=It might happen, but not likley") 
#     # print("Less than 60")
# if rand > 61 :
#     r = requests.post("https://api.telegram.org/bot1238646884:AAGUYD9VFsGQ8cF5BqRJWP_qxWIF43sA8kw/sendMessage?chat_id=-1001247118458&text=Its not happening today...") 
#     # print("Over 60")
# # extracting response text 
# # response = r.text 
# # print(response) 

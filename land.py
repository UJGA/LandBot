#!/usr/bin/env python3

import random
import telegram_send


import random


rand = random.randint(1,101)
print(rand)

randNum = str(rand)

telegram_send.send(messages=["Today " + randNum + "% of the land has been developed"])

if rand < 40 :
    telegram_send.send(messages=["Theres a chance!"])

if rand > 41 and rand < 60 :
    telegram_send.send(messages=["It might happen, but not likley"])
if rand > 61 :
    telegram_send.send(messages=["Its not happening today..."])
   
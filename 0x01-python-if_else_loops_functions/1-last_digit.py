#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDig = (number % 10) if number >= 0 else ((-number % 10) * -1)
if(lastDig > 5):
    print(F"Last digit of {number} is {lastDig} and is greater than 5")
elif(lastDig == 0):
    print(F"Last digit of {number} is {lastDig} and is 0")
elif(lastDig < 6 and lastDig != 0):
    print(F"Last digit of {number} is {lastDig} and is less than 6 and not 0")

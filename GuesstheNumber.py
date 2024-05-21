import random #pip install random

target = random.randint(1, 100)
chance = 5
attempt = 0

#using while true loops

while True:

    user = int(input("Guess the number between 1-100:"))
    attempt += 1

    #if else
    if user == target:
        print('you won')
        break
    elif user < target:
        print("small number") 
    elif user > target:
        print("Big number")

        #attemptss
    if attempt == chance:
        print("You lose The number was:", target)
        break 

    # we are using Random app in python for making this game 
    #you can also make 
    #@cheeku           
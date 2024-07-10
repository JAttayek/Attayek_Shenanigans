#THE THREE CUP GUESSING GAME

import random
from random import shuffle

print("Welcome to the three cup guessing carnival game!")
print("On the table, we have cups '1', '2', and '3' to choose from.")
print("We're going to start with the ball in cup 'two' and shuffle at random")
print("Then, you will guess which cup the ball is under! Ready???")

#Create a list of the thre "cups" with 'o' as the ball hidden within cup 'two'
balllist = [" ","o"," "]

#Shuffle list
def shuffled_list(balllist):
    shuffle(balllist)

    return balllist

#Ask user for cup guess
def player_guess():
    guess = " "
    while guess not in [1,2,3]:    
        guess = int(input("Pick a cup: 1, 2, or, 3:  "))

    return guess

#Check to see if user guess is correct
def guess_check(balllist,guess):
    if balllist[guess-1] == "o":
        print("Congrats!! You guessed correctly\n" + str(balllist))
    else:
        print("WRONG!!!!\n" + str(balllist))


#Game structure
mixed_list = shuffled_list(balllist)

guess = player_guess()

guess_check(balllist,guess)

# Homework 12.2
# File: HW_12p1_Task2_sweese.py
# Date:    18 November 2021
# By:      Sam Weese
# Section: 3
# Team:    027
#
# ELECTRONIC SIGNATURE
# Sam Weese
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# This progam takes allows the user to configure their settings for the game before
# allowing them to roll dice according to the set scores.

import random
# the below code was going to be how I originally calculated this, but I talked to
# Gabe and he said he didn't know that so I did it the other way
# using oop this would be much easier, due to easily accessing a player as an
# object
# class aPlayer:
#     def __init__(self, aName):
#         self.score = 0
#         self.name = aName
#     def printScore:
#         print(f"{self.name}: {self.score}")
#     def roll:
#         die1 = random.randint(1, 6)
#         die2 = random.randint(1, 6)
#         if die1 == die2:
#             return 2*(die1+die2)
#         return die1+die2
#     def



aEnd = -1
while aEnd <= 0:
    aEnd = int(input("What is the Winning Score?"))

p1Name = input("Enter player 1's name:")
p2Name = input("Enter player 2's name:")
p1Die = random.randint(1, 6)
p2Die = random.randint(1, 6)
while p1Die == p2Die:
    p1Die = random.randint(1, 6)
    p2Die = random.randint(1, 6)
if p1Die > p2Die:
    print(p1Name, " goes first!")
    p1Total = p2Total = 0
    iterationBool = True
    while p1Total < aEnd and p2Total < aEnd:
        if iterationBool != True:
            print(f"It is your turn {p1Name}")
        else:
            iterationBool = False
        input("Hit enter when ready")
        diceAdded = 0
        while diceAdded != 7:
            p1Total += diceAdded
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            diceAdded = die1 + die2
            if die1 == die2:
                diceAdded = diceAdded*2
            print(f"{p1Name} rolled a {die1} and a {die2}!")
            if p1Total >= aEnd:
                break

        if p1Total >= aEnd:
            print(f"{p1Name} is the winner!")
            break
        print(f"Current Scores: \n {p1Name}:{p1Total} \n {p2Name}:{p2Total} \n")
        print(f"It is your turn {p2Name}")
        input("Hit enter when ready")
        diceAdded = 0
        while diceAdded != 7:
            p2Total += diceAdded
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            diceAdded = die1 + die2
            if die1 == die2:
                diceAdded = diceAdded*2
            print(f"{p2Name} rolled a {die1} and a {die2}!")
            if p2Total >= aEnd:
                break
        diceAdded = 0
        if p2Total >= aEnd:
            print(f"{p2Name} is the winner!")
            break
        print(f"Current Scores: \n {p1Name}:{p1Total} \n {p2Name}:{p2Total} ")

if p2Die > p1Die:
        print(p2Name, " goes first!")
        p1Total = p2Total = 0
        iterationBool = True
        while p2Total < aEnd and p2Total < aEnd:
            if iterationBool != True:
                print(f"It is your turn {p2Name}")
            else:
                iterationBool = False
            input("Hit enter when ready")
            diceAdded = 0
            while diceAdded != 7:
                p2Total += diceAdded
                die1 = random.randint(1, 6)
                die2 = random.randint(1, 6)
                diceAdded = die1 + die2
                if die1 == die2:
                    diceAdded = diceAdded*2
                print(f"{p2Name} rolled a {die1} and a {die2}!")
                if p2Total >= aEnd:
                    p2Total += diceAdded
                    break

            if p2Total >= aEnd:
                print(f"{p2Name} is the winner!")
                break
            print(f"Current Scores: \n {p1Name}:{p1Total} \n {p2Name}:{p2Total} \n")
            print(f"It is your turn {p1Name}")
            input("Hit enter when ready")
            diceAdded = 0
            while diceAdded != 7:
                p1Total += diceAdded
                die1 = random.randint(1, 6)
                die2 = random.randint(1, 6)
                diceAdded = die1 + die2
                if die1 == die2:
                    diceAdded = diceAdded*2
                print(f"{p1Name} rolled a {die1} and a {die2}!")
                if p1Total >= aEnd:
                    p1Total += diceAdded
                    break
            diceAdded = 0
            if p1Total >= aEnd:
                print(f"{p1Name} is the winner!")
                break
            print(f"Current Scores: \n {p1Name}:{p1Total} \n {p2Name}:{p2Total} ")

print(f"Final Scores: \n {p1Name}:{p1Total} \n {p2Name}:{p2Total} ")

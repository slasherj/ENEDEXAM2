# Activity Python 1: Task 2
# File: ACT_Python_HeaderTemplate_TeamXXX_UCusername.py
# Date:    11/17/21
# By:      Quincy Crawford
# Section: 008
# Team:    103
#
# ELECTRONIC SIGNATURE
# Quincy Crawford

import math
import random
#inputs
WS = int(input(' Enter the winning score'))
P1name = input('Enter Player 1 Name: ')
P2name = input('Enter Player 2 Name: ')
P1 = 0
P2 = 0
P1initial = 0
P2initial = 0
turn = 0
while WS < 1:
    WS = int(input(' Enter the winning score'))
while P1initial == P2initial:
    P1initial = random.randint(1, 6)
    P2initial = random.randint(1,6)
    if P1initial < P2initial:
        turn = 2
    else:
        turn = 1
while P1 < WS and P2 < WS:
    input('Hit enter when ready\n')
    diceT = 0
    if turn%2 == 0:
        print("{0}'s Turn".format(P2name))
        while diceT != 7:
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            diceT = dice1 + dice2
            print('{0} rolled a {1} and a {2}'.format(P2name, dice1, dice2))
            if dice1 == dice2:
                P2 = P2+ diceT *2
            elif diceT == 7:
               turn = turn + 1
            else:
                P2 = P2+ diceT
    else:
        print("{0}'s Turn".format(P1name))
        while diceT != 7:
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            diceT = dice1 + dice2
            print('{0} rolled a {1} and a {2}'.format(P1name, dice1, dice2))
            if dice1 == dice2:
                P1 = P1+ diceT *2
            elif diceT == 7:
               turn = turn + 1
            else:
                P1 = P1+ diceT
    print('Current Scores:')
    print('{0}: {1}'.format(P1name, P1))
    print('{0}: {1}'.format(P2name, P2))
if P1 > P2:
    print("{0} is winner".format(P1name))
else:
    print("{0} is winner".format(P2name))
print('{0}: {1}'.format(P1name, P1))
print('{0}: {1}'.format(P2name, P2))

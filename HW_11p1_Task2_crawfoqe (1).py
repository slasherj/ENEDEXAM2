# Activity Python 1: Task 2
# File: HW_11p1_Task2_crawfoqe.py  
# Date:    8/11/2021
# By:      Quincy Crawford
# Section: 008
# Team:    103
#
# ELECTRONIC SIGNATURE
# Quincy Crawford

#inputs
T = float(input('enter T value between -10f and 125f: ' ))
Wc = str(input('Wc value sunny, cloudy, or raining: '))
H = float(input('H value between 0 and 1: '))

#Check inputs
x = 0
if T< -10 and T>= 125:
    print('invalud T input')
    x = 1
if Wc != 'sunny' and Wc != 'cloudy' and Wc != 'rainy': 
    print('Wc-value must be sunny, cloudy, or raining')
    x = 1
if H<0 or H > 1:
    print ('H value between 0 and 1')
    x = 1

if x==0:
    if Wc == 'rainy':
        print('work inside')
        if H > .8:
            print('give two 15 minute breaks')
        elif H > .9 and Hc == 'cloudy':
            print ('give one 15 minute break')
        else:
            print ('give one 10 minute break')
    elif T > 80 and T < 90 and H > .9 and Wc == 'sunny':
        print ('give two 10 minute breaks')
    elif T > 80 and T < 90 and H > .9 or Wc == 'sunny':
        print ('give one 10 minute breaks')
    else:
        print('no extra breaks')

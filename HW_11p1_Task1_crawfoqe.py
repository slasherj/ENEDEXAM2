# Activity Python 1: Task 1
# File: HW_11p1_Task2_crawfoqe.py  
# Date:    8/11/2021
# By:      Quincy Crawford
# Section: 008
# Team:    103
#
# ELECTRONIC SIGNATURE
# Quincy Crawford

import math

#Inputs
T = float(input('T-values that is in between -10F and 125F: '))
Wc = int(input('Wc values that are 0, 2, ir 3: '))
H = float(input('H-values between 0 and 1: '))
L = float(input('L-values >=0: '))
hSTRUC = float(input('hSTRUC-value that ranges between 20ft and 2800ft: '))
sDRY = int(input('sDRY-values that is 0, 2, or 3: '))

#Varify inputs
x = 0
if T < -10 and T >= 125:
    print('Invalid T. T must be between -10F and 125F. ')
    x = 1
if Wc != 0  and Wc != 2 and Wc != 3:
    print('Wc value must be 0, 2, or 3')
    x = 1
if H < 0 or H > 1:
    print('H value between 0 and 1')
    x = 1
if L < 0:
    print('L values must >= 0. ')
    x = 1
if hSTRUC < 20 or hSTRUC > 2800:
    print('hSTURC value must be between 20 and 2800. ')
    x = 1
if sDRY != 0 and sDRY != 2 and sDRY !=3:
    print('sDRY must be 0, 2, or 3. ')
    x = 1
#Program
if x == 0:
    HRI = 0.75*T+5*Wc+H**2
    if HRI > 75:
        Hcat = 1
        print('The site manager allows for 1 extra break')
    elif HRI < 75:
        Hcat = 0
        print('No extra break')

    FRI = 0.2*L+0.03*hSTRUC+30*Hcat+10*sDRY
    if FRI > 100:
        print('Hold saftey meeting')
    if HRI <= 100:
        print(" SAFTY IS JOB #1")
    print('The value of HRI is {0: .1f} /n' .format(HRI))
    print('The value of FRI is {0: .1f} /n' .format(FRI))

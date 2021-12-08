# Activity Python 1: Task 1
# File: ACT_Python_HeaderTemplate_TeamXXX_UCusername.py
# Date:    11/17/21
# By:      Quincy Crawford
# Section: 008
# Team:    103
#
# ELECTRONIC SIGNATURE
# Quincy Crawford

import math

#inputs
Vo = int(input('Enter intial velocity (m/s): '))

while Vo < 0:
    Vo = int(input('Enter intial velocity (m/s): '))
I = float(input('Enter angle increment in degrees: '))
while I < 0 or I > 90:
    I = float(input('Enter angle increment in degrees: '))

theta = I
g = 9.18

while theta < 90:
    MH = Vo**2*(math.sin(math.radians(theta))**2/(2*g))
    IT = (2*Vo*math.sin(math.radians(theta))/g)
    print('At angle {0:.2f} degrees, the max height is {1:.2f} and the inpact time is {2:.2f} \n'.format(theta,MH,IT))
    theta = theta + I

# Homework 12.1
# File: HW_12p1_Task1_sweese.py
# Date:    11 November 2021
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
# This program calculates the maximum height and impact time base off of a singular value,
# and then calculates subsequent values based off of this original value, using a print function
# and while loops.


import math

def defaultPrint(angle, impactT, maxHeight):
    print(
    "For Angle = {0:.2f} deg., Impact Time = {1:.2f} s and Max Height = {2:.2f} m".format(angle, impactT, maxHeight)
    )

initVelocity = 0
while initVelocity <= 0:
    initVelocity = float(input("Enter the initial velocity (in meters/second):"))


angleTheta = 0
while angleTheta <= 0 or angleTheta >= 90:
    angleTheta = float(input("Enter an angle increment:"))

i = 1
angleTheta2 = angleTheta
while angleTheta2 < 90:
    i += 1
    maxHeight = initVelocity**2 * ((math.sin(angleTheta2*math.pi/180))**2)/(2*9.81)
    impactTime = 2*initVelocity*math.sin(angleTheta2*math.pi/180)/(9.81)
    defaultPrint(angleTheta2, impactTime, maxHeight)
    angleTheta2 = i * angleTheta

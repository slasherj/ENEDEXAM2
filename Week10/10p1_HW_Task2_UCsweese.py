# Homework 10.2
# File: 10p1_HW_Task2_UCsweese.py
# Date:    4 November 2021
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
# This program takes inputes of impendences and phase constants of materials (and amipltude),
# and then returns angles and amplitudes
#

II1 = float(input("Please enter the intrinsic impedance of material "+ str(1)+":"))
PhaseConstant1 = float(input("Please enter the phase constant of material "+str(1)+":"))
II2 = float(input("Please enter the intrinsic impedance of material "+ str(2)+":"))
PhaseConstant2 = float(input("Please enter the phase constant of material "+str(2)+":"))
IncidentWave = float(input("Please enter the amplitude of the incident wave (V/m):"))

import math

II1 = float(377.14)
PC1 = float(3.08)
II2 = float(1131.42)
PC2 = float(2.11)
Amp = float(20)
B1 = PC1 **2
B2  = PC2 **2
N1 = II1 **2
N2 = II2 **2
sinBA = (B2*(N2-N1)/(N2*B1 - N1*B2))**(1/2) # good
ThetaBA = math.asin(sinBA) # good
ThetaT = math.acos((II1*math.cos(ThetaBA))/II2)
cosThetaT = math.cos(ThetaT)
cosThetaBA = math.cos(ThetaBA)
Et0 = 2*II2*math.cos(ThetaBA)*Amp/(II2*math.cos(ThetaT)+II1*math.cos(ThetaBA))
Er0 = (II2*cosThetaBA-II1*cosThetaT)*Amp/(II2*cosThetaBA+II1*cosThetaT)
print("Incident angle: {0: .2f} degrees".format(ThetaBA/math.pi*180))
print("Reflected angle: {0: .2f} degrees".format(ThetaBA/math.pi*180))
print("Transmitted angle: {0: .2f} degrees".format(ThetaT/math.pi*180))
print("Reflected amplitude: {0: .2f} V/m".format(Er0))
print("Transmitted amplitude: {0: .2f} V/m".format(Et0))

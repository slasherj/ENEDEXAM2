# Homework 11.1
# File: HW_11p1_Task2_sweese.py
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
# This progam takes temperature, weather conditions, relavtive humidity, structure height and the number of
# ladderes on a job site and calculates 2 indexes (HRI and FRI), from which it determines if the job site
# requires any intervention.


GlobalList =[]

def checkInput(value, name, min, max, list):
    if value < min or value > max:
         list.append(name)

def checkValues(value, name, listValid, list):
    for x in listValid:
        if value == x:
            return
    list.append(name)

T = float(input("Enter the temperature:"))
Wc = int(input("Enter weather conditions (0 for cloudy, 2 for partly cloudy, and 3 for sunny):"))
H = float(input("Enter relative humidity:"))
L = int(input("Enter number of ladders:"))
hStruc = int(input("Enter height of structure (in ft):"))
checkInput(T, "Temperature", -10, 125, GlobalList)
checkValues(Wc, "Weather Conditions", [3,2,0], GlobalList)
checkInput(H, "Humidity",  0, 1, GlobalList)
checkInput(hStruc, "Structure height", 20, 2800, GlobalList)
HRI = 0.75*T +5 * Wc + H**2

Hcat = 0
if (HRI > 75):
    Hcat = 1

Sdry = int(input("Enter the level of dryness:"))
checkValues(Sdry, "Dryness", [3,2,0], GlobalList)

FRI = 0.2 * L + 0.03 * hStruc + 30*Hcat + 10*Sdry

if len(GlobalList)!= 0:
    for x in GlobalList:
        print("{} has an invalid value!".format(x))
    exit(1)

retVal = ""
if HRI > 75:
    retVal += "Allow for one extra break. "
if FRI > 100:
        retVal +="Hold a safety meeting to remind workers of proper procedures to reduce fall related injuries."
if len(retVal) == 0:
    retVal = "Safety is Job #1"
print("{0:01f} is the HRI value, {1:01f} is the FRI value.".format(HRI, FRI))
print(retVal)

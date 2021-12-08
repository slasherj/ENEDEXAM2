# Homework 11.2
# File: HW_11p2_Task2_sweese.py
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
# This progam takes temperature, weather conditions, and relative humidity on a job site
# and calculates the safety breaks which need to be given.


GlobalList = []
def checkInput(value, name, min, max, list):
    if isinstance(value, float):
        if value < min or value > max:
             list.append(name)
        return
    list.append(name)

def endPrint(aStr, eCode =0):
    print(aStr)
    exit(eCode)

def checkValues(value, name, listValid, list):
    if not isinstance(value, str):
        list.append(name)
        return
    value = value.lower()
    for x in listValid:
        if value == x:
            return
    list.append(name)

T = float(input("Enter the temperature:"))
H = float(input("Enter relative humidity:"))
Wc = str(input("Weather conditions:"))
checkInput(T, "Temperature", -10, 125, GlobalList)
checkValues(Wc, "Weather Conditions", ["sun","cloudy","raining"], GlobalList)
Wc = Wc.lower()
checkInput(H, "Humidity", 0, 1, GlobalList)

if len(GlobalList) != 0:
    for x in GlobalList:
        print("%s is an invalid value!" % x)
    exit(1)

if Wc == "raining":
    print("Work inside!")
    exit(0)
if T >= 90:
    if H > 0.8 and Wc == "sun":
        endPrint("Give 2 15 minute breaks.")
    if H > 0.9 and Wc == "cloudy":
        endPrint("Give one 15 minute break.")
    endPrint("Give 1one 10 minute break.") # I am assuming 1one is a typo, but left it in for testing/grading purposes
if T > 80:
    if H > 0.9 and Wc == "sun":
        endPrint("Give two 10 minute break.")
    if H > 0.9 or Wc =="sun":
        endPrint("Give one 10 minute break.")
endPrint("No extra breaks.")

# CFU15.1
# File: CFU_15p1_Team027.py
# Date:    18 November 2021
# By:      Sam Weese Braden Kucera Akshat Rajora
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
# This progam takes prompts the user for a weight and type of alloy
# as long as either inputted value is incorrect it will prompt the user again for
# the value. It will return the cost of the alloy at the specified weight.

def CFU15p1():
    alloyNumber = int(input("Enter alloy number:"))
    alloyPounds = int(input("Enter number of pounds:"))
    while alloyNumber != 2024 and alloyNumber != 7075 and alloyNumber != 356:
        alloyNumber = int(input("That is an invalid alloy. Please enter a correct one. \n Enter alloy number:"))
    while alloyPounds < 0:
        alloyPounds = int(input("That is an invalid value. Please enter a correct one. \n Enter the alloy weight:"))
    if alloyNumber == 2024:
        print(f"That will cost {alloyPounds*140.875/100} dollars.")
    if alloyNumber == 7075:
        print(f"That will cost {alloyPounds*134.115/100} dollars.")
    if alloyNumber == 356:
        print(f"That will cost {alloyPounds*123.505/100} dollars.")

CFU15p1()

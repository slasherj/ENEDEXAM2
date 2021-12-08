# Homework 10.1
# File: 10p1_HW_Task1_UCsweese.py
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
# This program takes inputes and uses supplied equations to convert
# the inputs into impendence and amplitudes
#

Permittivity1 = float(input("Please enter the relative permittivity of material 1:"))
Permeability1 = float(input("Please enter the relative permeability of material 1:"))
Permittivity2 = float(input("Please enter the relative permittivity of material 2:"))
Permeability2 = float(input("Please enter the relative permeability of material 2:"))
InputedAmplitude = float(input("Please enter the amplitude of the incident wave (V/m): "))

def ImpendenceOfI(Permeability, Permitivity):
    return ((Permeability/Permitivity)**(1/2) )*377.14

def AmplitudeWaveOfI(Impendence1, Impendence2, Amplitude):
    return (2*Impendence2)/(Impendence1+Impendence2)*Amplitude

def TransmittedWaveOfI(Impendence1, Impendence2, Amplitude):
    return (Impendence2 - Impendence1)/(Impendence1 + Impendence2)*Amplitude
ImpRes1 = ImpendenceOfI(Permeability1, Permittivity1)
ImpRes2 = ImpendenceOfI(Permeability2, Permittivity2)


print("Intrinsic Impedance 1:" + str(ImpRes1)+ "Ohms")
print("Intrinsic Impedance 2:"+ str(ImpRes2)+"Ohms")

print("Transmitted Amplitude:" + str(TransmittedWaveOfI(ImpendenceOfI(Permeability1, Permittivity1), ImpendenceOfI(Permeability2, Permittivity2), InputedAmplitude))+ "V/m")
print("Reflected Amplitude:" + str(AmplitudeWaveOfI(ImpRes1, ImpendenceOfI(Permeability2, Permittivity2), InputedAmplitude))+ "V/m")

Perm1 = float(input("Please enter the relative permittivity of material 1:"))
Permeable1 = float(input("Please enter the relative Permeable of material 1:"))
Perm2 = float(input("Please enter the relative permittivity of material 2:"))
Permeable2 = float(input("Please enter the relative Permeable of material 2:"))
Amp = float(input("Please enter the amplitude of the incident wave (V/m): "))

ImpRes1 = (Permeable1/Perm1)**(1/2)*377.14
ImpRes2 = (Permeable2/Perm2)**(1/2)*377.14
WaveI = (ImpRes2 - ImpRes1)/(ImpRes1 + ImpRes2)*Amp
WaveR = (2*ImpRes2)/(ImpRes1+ImpRes2)*Amp

print("Intrinsic Impedance 1:" + str(ImpRes1)+ "Ohms")
print("Intrinsic Impedance 2:"+ str(ImpRes2)+"Ohms")

print("Transmitted Amplitude:" + str(WaveI)+ "V/m")
print("Reflected Amplitude:" + str(WaveR)+ "V/m")

# Class 11.1 Example
# Dr. Bucks

# import math library
import math

# get inputs from user
Rot_Speed = float(input('Please enter the rotational speed (RPM): '))
Diameter = float(input('Please enter the diameter: '))
Height = float(input('Please enter the height: '))
Density = float(input('Please enter the density: '))

# calculations
Rot_Speed = Rot_Speed*(2*math.pi)/60 # converted to rad/sec
Volume = math.pi*(Diameter/2)**2*Height
Mass = Volume*Density
KE = (Mass*(Diameter/2)**2*Rot_Speed**2)/4

# determine category
print('KE = {0} J'.format(KE))
if KE < 1e8:
  print('Fails')
elif 1e8 <= KE and KE <= 1e9: # can also be written as KE <= 1e9
  print('Ok')
else:
  print('Good')

# Date:    4/11/2021
# By:      Quincy Crawford
# Section: 008
# Team:    103

import math

#inputs

n1=float(input('enter the intrinsic impendance of material 1: ' ))
b1=float(input('enter the phases constant of material 1: ' ))
n2=float(input('enter the intrinsic impendance material 2: ' ))
b2=float(input('enter the phases constant of material 2: ' ))
ei0=float(input('enter amplitude of the incident wave (V/m): '))

theta_ba = math.asin((b2**2*(n2**2-n1**2))/(n2**2*b1**2-n1**2*b2**2))**.5
theta_t = math.acos(n1*math.cos(theta_ba)/n2)
theta_r = theta_ba

et0 = ((2*n2*math.cos(theta_ba))/n2*math.cos(theta_t))+n1*math.cos(theta_ba)*ei0

er0 = ((n2*math.cos(theta_ba)-n1*math.cos(theta_t))/n2*math.cos(theta_ba)+n1*math.cos(theta_t))*ei0

theta_ba = theta_ba/math.pi*180
theta_t = theta_t/math.pi*180
theta_r = theta_r/math.pi*180

print('incident angle: {0: .2f} degrees' .format(theta_ba))
print('reflected angle: {0: .2f} degrees' .format(theta_r))
print('transmitted angle: {0: .2f} degrees' .format(theta_t))
print('refelected amplitude: {0: .2f} degrees' .format(er0))
print('transmitted ampltitude: {0: .2f} degrees' .format(et0))

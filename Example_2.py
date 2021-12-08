# Example 2
# Dr. Bucks

# include the math library
import math

# get inputs from user - since both the temperature and the humidity can be
# decimal numbers, we convert the strings from the input statements into
# float values
T = float(input('Please enter the temperature in degrees C: '))
RH = float(input('Please enter the relative humidity as a decimal: '))

# perform calculations - note that we access the log function from the
# math library
f = (17.27*T)/(237.7 + T) + math.log(RH)
Td = (237.7*f)/(17.27 - f)

# display results
print('Dew Point Temperature = {0:.1f}'.format(Td))

# ENED1100, Spring 2020, Class 14p2 Example 3
# Dr. Bucks

# ask for input
x = int(input('Please enter a positive integer value in base 10: '))

# convert from decimal to binary
k = 0
while x >= 2**k:
    k = k + 1
k = k - 1

Result = ''
for n in range(k,-1,-1):
    a = x//2**n
    x = x - a*2**n
    Result = Result + str(a)

# display results
print('The value in binary is {0}'.format(Result))

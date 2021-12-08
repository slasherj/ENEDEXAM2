# Example 1
# Dr. Bucks

# part 1
print('Hello, my name is Joe.  What''s your name?')
Name = input('Please enter name: ')
# part 2
print('Hello, {0}.  How old are you?'.format(Name))
Age = int(input('Please enter age: '))
# part 3
Time2Hundred = 100 - Age
print('That means you will be 100 in {0} years.'.format(Time2Hundred))
print('That means you will be 100 in {0} years.'.format(100 - Age))
# Note: You can either do a calculation and store it in a variable
# prior to displaying it, or you can do the calculation directly in
# a print statement.  The two print statements above will produce the
# same results.

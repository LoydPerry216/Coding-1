# Discuss the anatomy of a function

# A function definition tells the computer
# the instructions on what we want to do with

# data = just means data types

# curly brackets = passing in data into
# the function definition. This is formally
# called a parameter

# parameter = placeholder for data

def modifyMyName(name):
    print('your new modified name is the great '+ name)
    
# when we pass data into a function call it is called an
# arguement
# argument = evidence, facts, real data.
#modifyMyName('Loyd')





# Lesson on Conditional Statements

# conditional statements use the 'IF' and 'ELSE'
#keywords to filler and create specific outcomes
#based on data.

def verifyAge(age):
    if age > 17: and age < 20:
        print('congrats! you can buy GTA VI')
    elif age > 20:
        print('Sorry, you need an adult to buy this game.')
else:
    print('Sorry, you need an adult to buy this game.')

verifyAge(69)
# what is a function

# A function is a set of instructions that peforms a specific
# task or job.

# there are two variations of a functions in Python
# Built-in Functions- instructions that are pre-written in python
#programming language.

# print() is a built in function. When we pass in data it will output
# it into the terminal automatically.
print('Coding Class')
# input() is a built in function. It allows us to write and pass in
# data into our program from the terminal
# name = input('what is your name?')
print()

number= int(input('please provide a number'))
print(23*number)

# User Defined Functions- custom functions written by engineers.

# Function Syntax - how it is written

#this is a function definition
def sandwichInstructions():
    print(' step 1. get 2 pieces of bread')
    print(' step 2. putting ingredients inside of the bread')
    print('step 3. put bread with ingredients together')

# there are two states of a user defined function;
    # the function definition
    # the function call

 #this is a function call

# 11/20/24

# functions using arithmetic operators

def depositMoney(x):
    checkAccount= 100
    print('money has been deposited successfully')
    print('new checking account balance is below: ')
    print(checkAccount - x)

depositMoney(35)
depositMoney(200)
depositMoney(95)

def withdraw():
    def checkAccountBalance():
        checkAccount = 1000
        print('here is your current check account balance:')
        print(checkAccount)

        checkAccountBalance()
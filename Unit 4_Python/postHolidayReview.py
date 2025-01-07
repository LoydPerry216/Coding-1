# data types - level 1: most basic building block of
# code . (numbers, letters, true or false)

# operators - level 2: the ability to manipulate and
# do things with data types
# (math, comparisions, assignment, etc.)

# functions - level 3: taking the first two concepts and
# organizing thes operations and data types
#into instructions

#conditional statements: level 3a: being able
# to add more control on our function intructions.


#Billing System Function.
# Goal: To be able to check and see if a user is past
# due or up-to-date on their subscription.

# user - username= string
# user - userPaymentDate = string/integer
# user - Payment Amount

# we need to know if their account is
# past due OR up-to-date

# function definition - tells the computer what the
# function actually does and how its supposed to work.
def checkSubscription(userDueDate, userMoneyInAccount):
   
   if userMoneyInAccount == True:
      print('subcripton is paid- auto withdraw payment.')
    else:
      print('payment still due- could not withdraw funds.')      

# function call - tells the computer to run our instruction

checkSubscription(7, False)
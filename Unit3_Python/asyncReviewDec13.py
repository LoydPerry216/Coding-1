#def integerDetection(x):
    #if x> 0:
        #print('this is positive')
    #elif x == 0:
        #print('this is a zero')
    #else:
        #print('this number is negative')        

#print(integerDetection(5))



#def movieTicketPriceByAge(age):
    #if age <= 10 and age > 0:
        #print('your ticket price is $5.00')
    #elif age > 11 and age < 20:
        #print('your ticket price is $10.00')
    #elif age >= 20 and age < 64:
        #print('your ticket price is $ 15.00') 
    #elif age >= 65:
        #print('your ticket is $5.00')
    #else:
        #print('Error. Something went wrong.Check your code')

#movieTicketPriceByAge(47)

# KEY POINTS
# - NEED TO CREATE DUSCOUNT PROGRAM BASED ON MEMBERSHIP
# - TO CREATE THIS FUNCTION I NEED THE NAME OF THE ITEM AND PRICE
# - AND MEMBERSHIP TYPE
# - WILL NEED TO USE MATH/ARITHMETIC AT SOME POINT


def discountFunction(membership, itemPrice):
    if membership == 'superShopper':
        print(' you are getting 10 percent off.')
        discount= itemPrice* .1
        total= itemPrice -discount
        print(discount)
        print(total)
    elif membership == 'megaShopper':
        print(' you are getting 15 percent off.')
        discount= itemPrice* .15
        total= itemPrice -discount
        print(discount)
        print(total)
    elif membership == 'ultraShopper':
        print(' you are getting 20 percent off.')
        discount= itemPrice* .2
        total= itemPrice -discount
        print(discount)
        print(total)        
    else:
        print('Error: sorry, tht membership type doesnt exist.')

discountFunction('superShopper', 120)            
        
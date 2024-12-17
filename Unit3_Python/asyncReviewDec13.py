#def integerDetection(x):
    #if x> 0:
        #print('this is positive')
    #elif x == 0:
        #print('this is a zero')
    #else:
        #print('this number is negative')        

#print(integerDetection(5))



def movieTicketPriceByAge(age):
    if age <= 10 and age > 0:
        print('your ticket price is $5.00')
    elif age > 11 and age < 20:
        print('your ticket price is $10.00')
    elif age >= 20 and age < 64:
        print('your ticket price is $ 15.00') 
    elif age >= 65:
        print('your ticket is $5.00')
    else:
        print('Error. Something went wrong.Check your code')

movieTicketPriceByAge(47)
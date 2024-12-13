#def check_number(num):
    #if num > 0:
        #return "This is a positive number."
    #elif num < 0:
        #return "This is a negative number."
    #else:
        #return "This is zero."

#print(check_number(10))   
#print(check_number(-12))  
#print(check_number(0))    



def get_ticket_price(age):
    if age >= 0 and age <= 10:
        return 5  
    elif age >= 13 and age <= 17:
        return 8  # Price for teens
    elif age >= 18 and age <= 64:
        return 12  
    elif age >= 65:
        return 7  
    else:
        return "Invalid age"
    
get_ticket_price(10)                                    

campingSupplies = ['tent', 'sleeping bag', 'flash light', 'camping knife']
def reverse_list():
    
    campingSupplies.reverse()
    return campingSupplies

reversed_supplies = reverse_list()
print(reversed_supplies)

def combine_lists():
    campingFood = ['marshmellows','gram crackers','chocolate','chicken hot dogs','water',]
    combined_list = campingSupplies + campingFood  
    return combined_list

combined_items = combine_lists()
print(combined_items)
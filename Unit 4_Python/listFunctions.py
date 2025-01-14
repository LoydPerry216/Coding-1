# lists = a data type for collecting and storing
# other data types into one variable.
# - We can store any data type inside of a list, including
# other lists.
# - We can store duplicate data inside of lists.
# - We can locate and access data in a list
# by its index postition.
# - Lists are changable. We can add and remove tyhings from
# them.

skii_trip_items= ['snow boots','heavy coat']\

# append() methond - allows us to add items to a list.
# the new added item will be added to the back of the
# list.

skii_trip_items.append('gloves')
skii_trip_items.append('thick socks')
print(skii_trip_items)

# insert() method - allows us to add an item to a list,
# and also dictate what postition that item will be at.
# insert takes two arguments, the index where you want to
# place the data, and the actual data.

skii_trip_items.insert(2,'goggles')
print(skii_trip_items)

#pop() method - allows us to remove the last item in a list
skii_trip_items.pop()
print(skii_trip_items)

# remove() method - allows us to remove an item from the last
# based specifically on the data's value.
skii_trip_items.remove('snow boots')
print(skii_trip_items)








def clothingBySeason():
    summerClothes = []
    winterClothes = []
    clothingSelection= input('what are u wearing')
    if clothingSelection =='tee-shirt':
        summerClothes.append('tee-shirt')
        


clothingBySeason()

def favoriteRestaurant()
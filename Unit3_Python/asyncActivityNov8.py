def reverse_word(word):
    return word[::-1]

print(reverse_word('pet'))
print(reverse_word('book'))

def state_landmark(state):
    if state =='Pennsylvania':
        return "A landmark in Pennsylvaina is Indpendence Hall, where the famous Declaration of Independence was signed"
    if state == 'New York':
        return "A landmark in New York is the Statue of Liberty, a famous gift from France"
print(state_landmark('Pennsylvania'))
print(state_landmark('New York'))
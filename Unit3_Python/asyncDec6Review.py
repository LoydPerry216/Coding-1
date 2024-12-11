def reverseWord(word):
    txt = "Hello World"[::-1]
    print(txt)

reverseWord('pizza party')


def landmarkByState(state):
    if state == 'PA':
        print('a landmark in Pa is the liberty bell in Philly.')
    elif state =='NY':
        print('A landmark in NY is the statue of liberty in NYC ')    
    else:
        print('The info on this states landmarks are unavailable.')    

landmarkByState('NY')
# BUBBLESORT
def BubbleSort(list):
    for iteration in range(len(list) - 1): #For each number in the length of the list
        for i in range(len(list) - 1): #for each position in the list
            if list[i] > list[i + 1]: #if value at index i of list is less than value at index i +1 of list, proceed
                #swapping
                temp = list[i] #create a variable to hold the value at index i of list
                list[i] = list[i +1] #value at index i of list is equal to value at index i + 1 of list
                list[i + 1] = temp #value at index i +1 of list is then equal to temporary value
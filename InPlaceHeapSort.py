# IN-PLACE HEAP SORT
def heapsort(list):
    length = len(list) - 1 #get length of the list
    middle = int(length / 2) #get middle fo the list
    for i in range(middle, -1, -1): #decrement the value in 'middle' value each time around the loop
        bubbledown(list, i, length) #recursively call the function, passing the list, the value of i and the length of the list
        #biggest item now at the front

    for i in range(length, 0, -1): #for each number in the range of the length of the list
        if list[0] > list[i]: #if the number at index 0 is less than the number at index i of the list, proceed:
            #swapping
            temp = list[0] #temporary value = value at index zero of list
            list[0] = list[i] #value at index 0 of list = value at index i of list
            list[i] = temp #value at index i of the list = temporary value
            bubbledown(list, 0, i - 1) #recursively call the move function passing the values

def bubbledown(list, first, last):
    while ((first * 2)+1) <= last: #while the first value multiplied by two plus one is less than or equal to the last value, proceed:
        child = (first * 2) + 1 #child value is equal to the first multiplied by two plus one
        temp = first #temporary value used for moving values
        if list[temp] < list[child]: #if temp value/index of list is less than child value/index of list, proceed:
            temp = child #update the temporary value to be the child value
        if (child + 1) <= last and list[temp] < list[child+1]: #if the child value plus one is less than or equal to the last value AND value of temp index of list is less than child + 1 index of list, proceed
            temp= child+1 #assign child +1 to temp
        if temp is not first: #if the temp variable is not at the first position, proceedL
            list[first], list[temp] = list[temp], list[first] #swapping values - swapping value at index first of list, with index temp of list
            first = temp #update the first variable to now be the value of temp
        else: #finished
            break #break out of the loop

# list = [41,37,35,62,29,39,54,27,60,25,40,56,51,48,43,51,43]
# heapsort(list)
# print('HEAPSORT:  ',list)
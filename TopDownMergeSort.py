# TOP-DOWN MERGESORT
#Mergesort from Lecture slides - http://www.cs.ucc.ie/~kb11/teaching/CS2516/Lectures/restricted/L05-MergeSort.pdf
def mergesort(list):
    length = len(list)
    if length > 1: #if the length of the list is not zero
        list1 = list[:length//2] #get the first half of the list
        list2 = list[length//2:] #get the second half of the list
        mergesort(list1)#recursively call function passing in first half of list
        mergesort(list2)#recursively call function passing in second half of list
        merge(list1, list2, list) #call merge function passing, list and two smaller lists (first half and second half)

def merge(list1, list2, list): #Function called by main program - mergesort
    f1 = 0 #variable one
    f2 = 0 #variable two
    while f1 + f2 < len(list): #while the sum of f1 and f2 are less than the length of the input list
        if f1 == len(list1): #if value f1 equals then length of the first half of the list (list1)daqfds
            list[f1+f2] = list2[f2] #number at index(f1 +f2) of input is rqual to index f2 of list2
            f2 += 1 #increment f2 by one
        elif f2 == len(list2): #otherwise if f2 value = length of the second half of the list (list2)
            list[f1+f2] = list1[f1] #list index(f1 + f2) value equals list1 index f1 value
            f1 += 1  #increment f1 by one
        elif list2[f2] < list1[f1]: #otherwise list2 value at index value f2 is less than list1 value at index value f1
            list[f1+f2] = list2[f2]#list index(f1 + f2) value equals list2 index f2 value
            f2 += 1 #increment f2 by one
        else: #otherwise
            list[f1+f2] = list1[f1]  #list index(f1 + f2) value equals list1 index f1 value
            f1 += 1 #increment f1 by one
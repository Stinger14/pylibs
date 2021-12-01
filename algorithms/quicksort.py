def quicksort(mylist):
    """Sort the mylist by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(mylist) > 1:
        pivot = mylist[0]
        for x in mylist:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return quicksort(less)+equal+quicksort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your mylist, just return the mylist.
        return mylist

list1 = [1,4,33,2,12,14,14.5]

quicksort(list1)
print(list1)
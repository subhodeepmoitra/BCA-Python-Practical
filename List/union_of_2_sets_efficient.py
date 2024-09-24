def myUnion(lst1, lst2): # makes the union of the 2 lists
    unionSet = [] # for the union set
    for item in lst1+lst2: # iterates over each element of list1+list2
        if not In(item, unionSet): # checks if In() returns T/F. Gets active if receives F from In()
            unionSet.append(item) # creates the union set
        #else:
        #    pass
    return unionSet
        
def In(element, lst): # for checking if an element repeats in the union set
    for i in lst: # iterates over every element in the union set
        if element == i: # if the iterated element matches with any element in the union set
            return True # True as "yes same element found in union list"
    return False # False as "no common elements found"


lst1 = [1,2,3,1,5,6]
lst2 = [2,4,6,7,9,1,5,8]

print(f"The union of {lst1} and {lst2} is {myUnion(lst1,lst2)}")
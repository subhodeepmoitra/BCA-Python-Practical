def myUnion(list1, list2):
    add = list1+list2
    union = noSimilarElement(add)
    return union

def noSimilarElement(list):
    flag =0 # for checking any problems
    noSimilarEle = []
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i] == list[j]:
                continue # terminate the current iteration and start a new iteration in 'i'
            else:
                if In(list[i], noSimilarEle): # In() is for checking if an element is in the list or not 
                    # If In() returns true then terminate the current 'j' loop and move to the next element
                    # move to next element as element is repeating so stop and move no need to take that in.
                    flag = 1
                    break
                if flag == 0: # no repeating element -> append current element from 'i' to list noSimilarEle
                    noSimilarEle.append(list[i]) 
                    break
        flag = 0 # reset the flag value to 0 default for a new iteration with 'i' loop... New iteration in 'i'
        # means new element in the list
    if In(list[0], noSimilarEle):
        pass # pass is a placeholder for further code/ unfinished block of code
    else:
        noSimilarEle.append(list[0])
    return noSimilarEle

def In(element, list):
    # checks for common elements in the list
    flag = 0
    for i in range(len(list)):
        if element == list[i]:
            flag = 1
    if flag == 1:
        return True
    else:
        return False 

list1 = [1,2,3,1,5,6] # 1 2 3 1 5 6 |||||| 1 2 1 4 5 2 6
list2 = [2,4,6,7,9,1,5,8] # 2 4 6 7 9 1 5 8 |||||| 2 1 6 7 4 7 9 3

print(f"Union of {list1} and {list2} is {myUnion(list1, list2)}")
def wordCount(text):
    count = 0 # holds the number of words
    inWord = False # flag to tell if we are inside a word or not

    for char in text:
        if not isLetter(char): # ignore the non-letters and characters means if isLetter returns True? else false
            inWord = False
        else:
            if not inWord: # checks if it is inside a word or not by checking whether True or False
                # If we are inside a word then the previous character would turn inWord True otherwise False
                # activates when inWord is False
                count += 1
            inWord = True
        #print(inWord) # Debugging statement for showing the status of True or False
    return count

def isLetter(char): # checks by the ASCII value as written inside single quotes
    return ('A' <= char <= 'Z') or ('a' <= char <= 'z') # returns True or False if alphabet is given returns True else False


text = input("Enter a phrase: ")
print(f"The word count is: {wordCount(text)}")

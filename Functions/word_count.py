def wordCount(text):
    count = 0 
    inWord = False # flag to tell if we are inside a word or not

    for char in text:
        if not isLetter(char): # ignore the non-letters and characters
            inWord = False
        else:
            if not inWord: # checks if it is inside a word or not by checking whether True or False
                count += 1
            inWord = True
        #print(inWord) # Debugging statement for showing the status of True or False
    return count

def isLetter(char): # checks by the ASCII value as written inside single quotes
    return ('A' <= char <= 'Z') or ('a' <= char <= 'z') # returns True or False


text = input("Enter a phrase: ")
print(f"The word count is: {wordCount(text)}")

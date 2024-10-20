import string

def countOccurances(text):
    text = text.translate(str.maketrans('','',string.punctuation)) #removes the punctuations
    word = text.split() #extracts the words from the raw text
    uniqueWords = set(word) #convert to set as sets don't hold duplicate values
    wordCount = {} #dictionary that stores the words (key) and count (values)
    
    for unique_words in uniqueWords: #iterating through the set
        count = 0 #counter for checking the occurances of words
        for w in word: #iterating through the raw string without punctuations
            if w.lower() == unique_words.lower(): 
                count += 1
        wordCount[unique_words.lower()] = count 
    return wordCount
    

text = input("Enter a string: ")

occurances = countOccurances(text)
print(occurances)
def main():
    text = input("Enter a phrase to be converted to Pig Latin: ")
    newText = text.split()  # convert string into a list of each word
    newList = []  # creating a new list to add all the new elements
    for word in newText:
        # checking if the word is a punctuation so the "ay" is not added to it
        # and the word is just added to the string
        if (word == "!" or word == "?" or word == "," or word == "."):
            newList.append(word)
        else:  # otherwise move the first letter to the front and add "ay" to the string
            wrd = word[1:] + word[0] + "ay"
            newList.append(wrd)  # append the new word to the new list
    n = ' '.join(newList)  # convert the list back to a single string
    print(n)
    main()

main()
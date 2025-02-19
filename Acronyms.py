# Asking the user to enter a phrase and storing it as a string
phrase = input("Enter a Phrase: ")
# Splitting the user input phrase into a list of words
text = phrase.split()
# Initializing an empty string to store the acronym value
acronym = " "
# Iterating through each word in the list
for i in text:
    # Taking the first letter of each word, converting it to uppercase, and appendding it to 'acronym variable'
    acronym = acronym + str(i[0]).upper()
# printing the output
print(acronym)
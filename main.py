#I will do multiple examples of the string methods present in the Table 4.2 in our chapter

data = "This is the life!"
print(" > String:", data)

#center a string within a given width
print("\ns.center(width):")
print(data.center(25))

#count how many occurences of a character in a string
print("\ns.count(sub [, start [, end]]):")
print(data.count('i'))

#ask if the string starts with a certain character(s)
print("\ns.startswith(sub):")
print(data.startswith("This"))

#ask if the string ends with a certain character(s)
print("\ns.endswith(sub):")
print(data.endswith("life!"))

#find what position a certain character starts
print("\ns.find(sub [, start [, end]]):")
print(data.find("the"))

#ask if the string is only letters
print("\ns.isalpha():")
print(data.isalpha())

#ask if the string is only digits
print("\ns.isdigit():")
print(data.isdigit())

#seperates multiple text items in a string into a sequence of each text item
print("\ns.split([sep]):")
words = data.split()
print(words)

#combines text items in a sequence.  Can also be used to add in words into an existing string
print("\ns.join(sequence):")
print("".join(words))
print(" ".join(words))

#makes all letters in a string lowercase
print("\ns.lower():")
print(data.lower())

#makes all letters in a string uppercase
print("\ns.upper():")
print(data.upper())

#replaces a character or text item in a string with something else given
print("\ns.replace(old, new [, count]):")
print(data.replace("the","some"))
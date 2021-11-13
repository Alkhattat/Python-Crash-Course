# Hello there, how old are you?- What index will return "how old"
word = "Hello there, how old are you?"
word [13:20]
print(f"word [13:20]")


# story = "Python is awesome" - What is story[2:4] + story[-1]
story = "Pytho is awesome"
story[2:4] + story[-1]
print(f"story[2:4] + story[-1]")


# mystring = "Python rocks" What is len(mystring)?
mystring = "Python rocks"
len(mystring)
print(f"len(mystring) is: {len(mystring)}")


# flower = "Rose" What is flower[0] = "P" ; print(flower)? Will it return "Pose"

flower = "Rose"
flower[0] = "P" ; print(flower)



# word = "python is so cool"- What is word[-4:] * 3
word = "python is so cool"
word[-4:] * 3
print(f"word[-4:] * 3 is: {word[-4:] * 3}")

# Write a code that returns "pepsi" as "PEPSI"
soft_drink = "pepsi"
soft_drink.upper()
print(f"soft_drink.upper()")



# Write a code that returns "macdonald" as "MacDonald"
word1 = "mac"
string = word1.capitalize()
word2 = "donald"
word2.capitalize()
string2 = word2.capitalize()
print(string + string2)


# Write a code that returns "MUSHRAH" as "mushrah"
word = "MUSHRAH"
word.lower()
print(word.lower())


# Using the built-in method, how will you "Hello World" as a list?
word = "Hello World"
word.split()


# How do I add a "-" in between every character in a string "Python is cool"?
string = "Python is cool"
print('-'.join(string))


# How do I remove "Hello" from "Hello World"
word = "Hello World"
word[-6:12]
print(word[-6:12])


# What is the index of the first character in a string?
name = "Murshid"
name[0]
print(name[0])


# Using one of the string built-in method, print out the numbers of 'o' in the string "Hello , python is sooo cool"
string = "Hello, python is sooo cool"
string.count("o")
print(string.count("o"))


# If I want to write this string: "hello world! welcome to Python" as a title case, what inbuilt method of python will I call
string = "Hello world! welcome to python"
string.title()
print(string.title())


# Convert this string to a title case: "Hello world! welcome to python"
string = "Hello world! welcome to python"
string.title()
print(string.title())

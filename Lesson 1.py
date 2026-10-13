# The letters in indigo are considered functions
# Some functions have return values (Getting input and then "handing" the input back )
# Variables-a container for a value inside a computer/program
# Variables are white
# = sign is the assignment operator
# (Copies from the right to the left)

name = input("Enter your name: ")
# name = name.strip()
#Strips the whitespace from str
# name=name.title()
# Makes every starting letter of every word capitalized
#Input automatically converts inputs into str

name = name.title().strip()
# You can compound your functions

first, last= name.split(" ")
# Splits users first and last name

# Comments - notes to yourself like using # that are in gray
# Comments can be "pseudocode", which is using human language to outline your program

print("Hello, ", end="")
print(name)
# Strings are texts of words
# str is the abbreviation
# Inputs require strings, which are in quotations
# Arguments - inputs/data stored in a function
# Some functions can pass in multiple inputs using a comma
# \n means new line; that means by default, the print function automatically adds a new line
# print has an end="\n"
# you have to put the end parameter and sep parameter at the end of the function

# You can make your own functions
# docs.python.org/3/library/functions.html is the page for where all the documentation for the functions are
# Parameters and arguments are the same thing
# but parameters are what functions can take, and arguments are the actual inputs you put in

print("I like", "To fly", "Paper Rockets", sep=" 🚀")
# sep= ' ' means the function automatically adds whatever is in the quotes
# end= means the function automatically adds whatever in the quotes at the end of the function
# you have to put the end parameter and sep parameter at the end of the function

print("Hello, "+name)
# + operator is more of conjoining things rather than addition

# Positional Parameters - identified by their order in a function
# Names Parameters - identified by their names

print("Hello, \"friend\"")
# To make quotations in a string, you do "" inside, or outside and '' inside or outside
# you can also use the \

print(f"Hello, {first}")
# f string/ format string
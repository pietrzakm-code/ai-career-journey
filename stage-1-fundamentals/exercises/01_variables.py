#this file is just to learn - not a good example of programming
#no file should look like that

#print to console
print("Hello World!")

#print multiple lines
print("Line 1")
print("Line 2")
print("Line 3")

#multiple functions in one line
print("print1"); print("print2"); print("print3")

#print function parameter : end
print("This", end = " ")
print("is", end="\t")
print("not the end of line")
print("That was.", end = "\n\n")

#print numbers
print(4, end =", ")
print(532, end = ", ")
print(123.234)

#print math result
print(2+2, end = ", ")
print(5/21, end = ", ")
print((2+3)*4)

#print mixed string and numbers
print("2+2=", 4, " and 4+5=", 4+5,sep = "")

#this is a comment
print() #you can also put comment in here
"""
I hate that kinds of comments
takes too much attantion.
It is a distraction.
Every comment like that should be in documentation,
or a function that needs comment like this should be simplified.
Uncle Bob would be proud
"""

#variables
x = 5
y = "john"
print(x, y, end = " - ")

x = "bob"
print(x)

#casting
x = str(4)
y = float(3)
z = int(3.5)
print(x, y, z)

#type of variable
x = 1
y = "John"
print(x, type(x), type(y))

#strings - check
x = 'John1'
y = "John2"

print(x, "is type of", type(x))
print(y, "is type of", type(y))

#variable names
camelCase = "each Word, Except The First, Starts With A Capital Letter."
PascalCase = "Each Word Starts With A Capital Letter."
snake_case = "Each_word_is_separated_by_an_underscore_character."

#multiple values to multiple variables
x, y, z = "John", "Rose", 345
print(x, y, z, sep = ", ")

#one value to multiple variables
x = y = z = 0.0
print(x, y, z, sep = ", ")

#collections
cars = ["volvo", "ford", "toyota"]

#unpack list
x, y, z, = cars
print(x, y, z)

#print output with +
print(x+y+z)
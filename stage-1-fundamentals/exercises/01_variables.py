#This file is just to learn variables and operations 
#Not a good example of programming
#No file should look like that


# --- PYTHON ----------

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


# --- PRINT ----------

#print to console
print("Hello World!")

#print numbers
print(4, end =", ")
print(532, end = ", ")
print(123.234)

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

#print mixed string and numbers
print("2+2=", 4, " and 4+5=", 4+5,sep = "")


# --- DATA TYPES ----------

#variables
x = 5
y = "john"
print(x, y, end = " - ")

x = "bob"
print(x)

#variable names
camelCase = "each Word, Except The First, Starts With A Capital Letter."
PascalCase = "Each Word Starts With A Capital Letter."
snake_case = "Each_word_is_separated_by_an_underscore_character."

#use UPPERCASE letters for constatn variable - in python there is no const
normal_variable = 10
CONST_VARIABLE = 20

#casting
x = str(4)
y = float(3)
z = int(3.5)
print(x, y, z)

#type of variable
x = 1
y = "John"
print(x, type(x), type(y))

x = 'John1'
y = "John2"
print(x, "is type of", type(x))
print(y, "is type of", type(y))

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

#merge
print(x+y+z)

#conversion/cast
x = 5.03
y = 3
z = "55"

print(int(x), float(y), 10 - int(z))


# --- NUMBERS ----------

#large numbers zero divider
print("The number 1000000000 ["+str(1000000000)+"] is the same as the number\n \
1_000_000_000 ["+str(1_000_000_000)+"]")

#print math result
print(2+2, end = ", ")
print(5/21, end = ", ")
print((2+3)*4)

#scientific notation
print(35e3, 12E3, -2.32e4)

#complex
x = 3+5j
y = 2j
z = -10j
print(x, y, z)

#logical operators
print(True and False)
print(True or False)
print(not False)

#math
print(1+2+3+4)
print(1-5)
print(5/2)
print(3*5)
print(2**10)
print((2+2)*5/2)


# --- STRING ----------

#format already existing text
text = "  Jan kowalski , alicja NoWak "
print(text.upper(), text.lower(), text.title())
print(text.strip(), text.lstrip(), text.rstrip(), sep = '|', end = "|\n")

#replace string with string
x = "to jest string"
print(x.replace("t", "l"))

#string get by index and slice
x = "to jest string"
print(x, x[3], x[:4], x[3:7], x[5:])

#for loop in string
x = "to jest string"
for letter in x:
    print(letter)

#check if "text" is in string
x = "to jest string"
print("jest" in x)
print("nie ma" in x)

#split string
x = "to jest string"
a, b, c = x.split(" ")
print(a, b, c, sep = " | ")

#format string
x = "to jest string"
y=43.2
format_text = f"Mozna dodac {2+2} coś i mozna dodac zmienna {x} ale nie tylko string {y}"
print(format_text)

#special characters
print("\'\\\t\"")


# --- Operators ----------

#identity
x = ['bmw', 'volvo']
y = ['bmw', 'volvo']
z = x

print(x is z)
print(x is y)
print(x==y)
print(x==z)

#membership
x = ['bmw', 'volvo', 'fiat', 'ford']

print('fiat' in x)

#bitwise
print(f"6[{6:08b}] and 3[{3:08b}]")
print(f"6 & 3 [{(6 & 3):08b}]")
print(f"6 | 3 [{(6 | 3):08b}]")
print(f"6 ^ 3 [{(6 ^ 3):08b}]")
print(f"6 << 3 [{(6 << 3):08b}]")
print(f"6 >> 3 [{(6 >> 1):08b}]")


#String delaration

a="string"
print(type(a))

#string convert

x=3
x=str(4)
print(type(x))

#Multiline Strings
#You can assign a multiline string to a variable by using three quotes:
#You can use three double quotes: OR You can use three Single quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Strings are Arrays

a="Hello, World!"
print(a[8])

#String Length

a="Hello, World!"
print(len(a))

#Check String

txt = "The best things in life are free!"
print("free" in txt)



#Use it in an if statement: in check string

txt_check="Somethink is went to wrong"
if "to" in txt_check:
 print("yes")


# NOt in check

txt_check="Somethink is went to wrong"
if "free" not in txt_check:
 print("yes")

#The upper() method returns the string in upper case:
 print("some Think is went wrong".upper())

#The lower() method returns the string in lower case:
print("SomeThink is went wrong".lower())

#Remove Whitespace strip()
#The strip() method removes any whitespace from the beginning or the end:
print("    SomeThink is went wrong  ".strip())

#String Replace
#The replace() method replaces a string with another string:

print("SomeThink is went iss wrong".replace("iss","to"))

#Split String
"""The split() method returns a list where the text between the specified
separator becomes the list items."""
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#Capitalize
"""Python String capitalize() method returns a copy of the
string with only its first character capitalized."""

print("some Think is went wrong".capitalize())

#String Concatenation

a = "Hello"
b = "World"
c = a + b
print(c)

#To add a space between them , add a "":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#String Formating

#example 1
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


#example 2
"""The format() method takes unlimited number of arguments,
and are placed into the respective placeholders:"""

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#example3
"""You can use index numbers {0} to be sure the arguments
are placed in the correct placeholders:"""

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))








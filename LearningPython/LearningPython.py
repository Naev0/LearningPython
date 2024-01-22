# this is how comments are made
# primatives
w = 4
x = -3
# x and y are integer, an integer is any whole number, be it negative or positive
# : any number that is not a fraction
y = 1.24131
# a float (floating point number) is any number that is not an integer
# namely it is any number that has a decimal
z = 1j
# j is used for complex numbers representing the imaginary part, rather than i as in normal maths.
print(type(w))
print(type(x))
print(type(y))
print(type(z))
# Booleans are logical operators, and when talking about computing it means a binary value of "true"
# or "false"
print(50 > 15)
print(12 == 2)
print(100 < 1000)
# When running "IF" statements, a type of Logical operation, Python works with Boolean "true" or "false" 
a = 200
b = 30
if a > b:
    print("a is greater than b!")
else:
    print ("b is NOT greater than a!")
# above we used the strings "a is greater than b!" and "b is NOT greater than a!
    # A string is any information surrounded by single or double quotes, these are typically reserved 
    # for plain-text, non variable uses *however* you can assign a variable to a string
c = "this is a string in a variable"
print(c)
# important note, strings are arrays of bites representing unicode characters. Square brackets can be
    # used to access elements of the string. *remember arrays start at 0, not 1*
d = 'hello world!'
print(d[1])
for t in 'banana man me want a tan':
    print(t)
# notice above that we used a variable that we had previously defined. This is possible and important
    # because variables can be reasigned at will Variables do not need to be declared 
    # with any particular type, and can even change type after they have been set.
    # however, variables can be Global or Block, just like JS and HTML.
xx = 1 # int
xy = 2.8 # float
xz = 1j # complex

# convert int to float
aa = float(xx)

# convert from float to int
bb = int(xy)

# convert from int to complex
cc = complex(xx)

print(xx)
print(xy)
print(xz)
print(type(xx))
print(type(xy))
print(type(xz))

print(aa)
print(bb)
print(cc)

print(type(aa))
print(type(bb))
print(type(cc))
print('--------------------------------------------------------')
#Python has no command for declaring a variable.
#A variable is created the moment you first assign a value to it.
# casting is what it is called when you assign the data type of a variable "str" "float" "int"
# you can get the data type of a variable with the "type()" function, like I did a second ago.
# variables are case-sensitive, they can include numbers and non-letter characters 

# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).
# Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

"""Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data,
the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets"""

thisList = ["apple", "banana", "orange", "pear"]
print(thisList)
"""List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.
When we say that lists are ordered, it means that the items have a defined order,
 and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list."""
# Lists are changeable, meaning that we can change, add, and remove items in a list after
# it has been created. Since lists are indexed, lists can have items with the same value.
# you can find the lenght of a list using the "len()" function
print(len(thisList))
print(type(thisList))
# From Python's perspective, lists are defined as objects that have the data type "list"
# you can also use the "list()" constructor when creating a new list rather than square brackets
thatList = list(("Volvo", "Honda", "Chevy", "Nissan")) # note the double round-brackets
print(thatList)
"""There are four collection data types in the Python programming language:

LIST is a collection which is ordered and changeable. Allows duplicate members.
TUPLE is a collection which is ordered and unchangeable. Allows duplicate members.
 -- Tuples have the data type "tuple" are ordered, unchangable, and are written in round brackets
SET is a collection which is unordered, unchangeable, and unindexed. No duplicate members.
DICTIONARY is a collection which is ordered and changeable. No duplicate members."""

# strings and lists both allow you to grab specific items from them using "[]" Where in a string,
# it counts each character, in lists it counts each item. Remember, the first item index is 0, not 1
print(thatList[1])
print(thisList[3])
# you can also use "negative indexing" which starts counting from the end, rather than the start
print("-------------------")
print(thatList[-1])
print(thisList[-3])
"""You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.
"""
anotherList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(anotherList)
print(anotherList[2:5])

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included
# you can also leave the first or last value in the index and it will list all items from the beginning
# up to the listed position, or from the listed position until the end, respectively.
# to check if an item is in a list, us an "if in" function: "if x in y: print("bazinga")" kinda deal
# I imagine the above "if in" check would be useful for huge lists, where you could easily check a large
    # list of items to see if something specific is in it. But it seems kinda clunky
# you can change items in a list by refrencing the item number. "thisList[1] == "blah blah blah""
# same thing for range if item values, [2:5] does the same thing, just gotta put that = in there.
# to add items to a list, without replacing any of the existing values, use the "insert()" function
# "insert()" will insert the item at the specified index.
print(thisList)
print("-----------------------------------------------")
print("notice how 'Watermelon' is added newly into the second list")
print("-----------------------------------------------")
thisList.insert(2, "Watermelon")
print(thisList)
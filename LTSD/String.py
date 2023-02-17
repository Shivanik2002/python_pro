string = "helloworld"
print("string")
print(string[0])
print(string[1:2])
print(string[0:])
print(string[2])
print(len(string))             # # len() returns the number of elements in a specified string
print(sorted(string))           # sorted() returns a string list of the specified iterableobject
print(string[-1])
print(type(string))
print(string.count("l"))          # # returns count of the element in the list
print(string.endswith("he"))        # Returns the number of times a specified value occure in a string
print(string.endswith("py"))        # Returns true if the string ends wit the specified value
print(all(string))
print(string.capitalize())                    # converts the first character to upper case
print(string.replace("helloworld","python"))        # rturns a string where a specified value is replaced with a specified value
x = string.lower()               # converts a string into lower case
print(x)
print(string.upper())            # converts a string into upper case
x = string.find("world")          # searches the string for a specified value and returns the position of where it was found
print("after find:",x)

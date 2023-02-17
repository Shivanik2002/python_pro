dict1 = {"january":1,"febuary":2,"march":3,"april":4}
print(dict1)
print(type(dict1))
print(dict1.values())         # Returns a list of the values in the dictionary
print(dict1.keys())           # Returns a list containing the dictionary's keys
print(len(dict1))             # len() returns the number of elements in a specified dictionary
print(max(dict1))             # it returns an item from the list with a max value             
print(min(dict1))             # it returns an item from the list with a min value
print(dict1.pop("january"))   # Removes the element with the specified key
print(dict1.items())          # Returns a list containing a tuple for each key value pair
print(dict1.get("march"))     # Return  the values of the specified key
print(dict1.copy())          # returns a copy of the dictionary
print(dict1.clear())         # Removes all the elements from the dictionary

dict2 = {1:"sunday",2:"monday",3:"tuesday",4:"wednesday"}
print(dict2)
print(dict2.fromkeys(dict2))
print(dict2.fromkeys(dict2,2))      # Return a dictionary with the specified keys and value
print(any(dict2))
dict1.setdefault(5,"thursday")        # returns the value of the specified key. if the key does not exist:insert the key,with the specified value
print(dict2)
print(dict2.popitem())          # # removes the last insrted key-value pair

dict1 = {"january":1,"febuary":2,"march":3,"april":4}
dict2 = {1:"sunday",2:"monday",3:"tuesday",4:"wednesday"}
dict1.update(dict2)             # updat the dictionary with the specified key-value pairs
print("After upadte:",dict1)
dict1.pop(1)                     # removes the element with the specified keys
print("After pop:",dict1)
dict2.popitem()             # removes the last insrted key-value pair
print("After popitem:",dict2)


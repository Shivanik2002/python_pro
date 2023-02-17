list1 = [12,23,45,89,107,546,132]
list2 = [34,45,890,2350,78,36,31]
print(list1,list2)
type(list1)         # type() method returns class type of the argument(object) passed as parameter in python
list1.copy()             #returns a shallow copy of the list
print("copy:",list1)         
print(max(list1))         # it returns an item from the list with a max value
print(min(list2))         # it returns an item from the list with a min value
print(sum(list1))          # sum of the numbers in the list is required everywhere
print(any(list1))         # any() returns True if at least one item of the iterable is True
print(all(list1))         # it will return false if the iterable is empty
print(len(list1))        # len() returns the number of elements in a specified list
print(sorted(list1))        # sorted() returns a sorted list of the specified iterableobject
list1.append(123)
print("append:-",list1)           # add a single element to the end of the list
list1.reverse()
print("reverse:-",list1)           #reverse the list
list1.append(list2)
print("append:-",list1)            # add a single element to the end of the list
list1.extend(list2)
print("extend:-",list1)             # adds iterable element to the end of the list
list2.pop()                       # removes element at the given index
print(len(list2))              
list2.sort()                    # sorts elements of a list
print("sort:-",list2)             
list2.insert(2,12)
print("insert:-",list2)          # insert an element to the list
list1.remove(12)
print(list1.count(34))         # returns count of the element in the list
sl = list1[::2]
print("slice:-",sl)             # slice() function returns a slice object that is used to slice any sequence
sl = list2[4:]
print(sl)
sl = list1[-1:]
print(sl)
sl = list1[:2]
print(sl)
index = list2.index(890)           #  index method returns the inde of the specified element in the list
print("Index:-",index)
list1.clear()            # removes all items from the list
print("clear:-",list1)
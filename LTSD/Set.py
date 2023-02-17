s = set()
print(type(s))
s1 = {"nayra","anita","shreya","prita"}
print(s1)
print(min(s1))            # it returns an item from the list with a min value
print(max(s1))           # it returns an item from the list with a max value
print(any(s1))           # any() returns True if at least one item of the iterable is True
print(all(s1))           # it will return false if the iterable is empty
print(len(s1))          # len() returns the number of elements in a specified set
s.add("shivani")            # adds a given element to a set
print("set after updating:-",s)

s2 = {12,34,56,789,879,24,24}
print(s2)
print(len(s2))               # len() returns the number of elements in a specified set
print(s2.copy())         # returns a shallow copy of the set
print(s2.discard(24))       # removes the element from the set
print(s2.update(s2))            # update the set with another set. or any other iterable
print(s2.remove(56))           # Removes all elements from the set
s1.intersection(s2)             # returns a set that is the intersection of two or more sets
print("After intersection:-",s2)
s1.intersection_update(s2)     # intersection_update() method is used to update a set with common elements
print("After intersection_update:-",s2)
s1.union(s2)                               #Return a set containing the union of sets
print("After union:-",s2)
s3 = s1.symmetric_difference(s2)
print("After symmetric_difference:-",s3)          #returns a set with the symmetric difference of two sets
print(s2.clear())           #  Removes  all  elements from the set
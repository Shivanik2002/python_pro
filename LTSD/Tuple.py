a = (12,34,56,89,908,56,29,678,345,98)
print(a)
print(len(a))       # this method returns total length of the tuple
print(max(a))        # this method returns largest element of a tuple
print(min(a))         # this method returns smallest element of a tuple
print(sorted(a))       # sorted() returns a sorted list of the specified iterable object
print(tuple(a))         # tuple() function is built in function in python that can be used to create a tuple
print(type(a))
print(sum(a))         # find the sum of the elements in a tuple
print(any(a))          # any() returns True if at least one item of the iterable is True
print(all(a))         # it will return false if the iterable is empty
print(a[-1])
print(a[::4])
print(a[:-2])
print(a[::-4])
print(908 in a)
print(999 in a)

b = ("shivii","rani","nidhi","palak")
print(b)
print(list(b))        
print(set(b))        # any iterable sequence like tuple
print(tuple(b))            # tuple() is used to create a tuple from different types of values
print(b.index("nidhi"))         # this method is used to find first indx position of the value in a tuple
print(b.count("palak"))          # this function is used to count and return number of times a value exists in a tuple
c = list(b)
c[1] = "shreya"
b = tuple(c)             # tuple() is used to create a tuple from different types of values
print(b)

c = a + b
print(c)
tup = ("shivii")
print(type(tup))       # type() function is used to get the type of an object
tup1 = ("rani")
print(type(tup1))
tp = ()
print(type(tp))
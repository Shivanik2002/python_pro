class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name},{self.age}"

p1 = Person("jai", 36)

print(p1)



print("____________________________________________")

# A class

class sub:
    # A simple class
    # attribure

    attr1 = "shivani"
    attr2 = "kushwah"

    # A sample method

    def fun(self):
        print("I'm ", self.attr1)
        print("my surname is",self.attr2)

# Driver code
# Object instantiatio

obj = sub()

# Accessing class attributes
# and method throught objects

print(obj.attr1)
obj.fun()
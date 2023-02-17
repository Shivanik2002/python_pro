(1).
# abstact base class work

from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self) :
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Dog(Animal):
    def move(self):
        print("I can bark")

class Lion(Animal):
    def move(self):
        print("I can roar")

#Driver code

S = Human()
S.move()

K = Snake()
K.move()

S = Dog()
S.move()

K = Lion()
K.move()


print("*************************************************")

(2).
# implementation of abstract
# class throught subclassing
import abc

class parent:
    def good(self):
        pass

class child(parent):
    def good(self):
        print("child class")

# Driver code

print(issubclass(child,parent))
print(isinstance(child(),parent))
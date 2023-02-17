class Demo:
    x = 20       # public variable
    _y = 30       # protected variable
    __z = 40       # private variable

    def method1(self):
        print("Hello I am public method")

    def __method2(self):
        print("Hello I am private method")

    def method3(self):
        self.__method2()

d = Demo()               
d.method1()


print("******************************************")


class Employee:
    # constructor
    def __init__(self, name, salary, project):
        # data members
        self.name = name
        self.salary = salary
        self.project = project

    # method
    # to display employee's details
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)

    # method
    def work(self):
        print(self.name, 'is working on', self.project)

# creating object of a class
emp = Employee('sneha', 8000, 'NLP')

# calling public method of the class
emp.show()
emp.work()


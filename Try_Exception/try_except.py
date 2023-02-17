def divide(x,y):
    try:
        print(f"{x}/{y} is {x/y}")
    except ZeroDivisionError as e:
      print(e)
    else:
        print("divide() function worked fine.")
    finally:
        print("close all the resources here")

divide(10,2)
divide(10,0)
divide(10,4)                    



print("_________________________________________________")

def divide_by(numerator,value,value1):
    result = 0
    try:
        result = numerator/value

    except ZeroDivisionError:

        try:
            result = numerator/value1

        except ZeroDivisionError:
            print("zero division error")
        else:
            print("operation succeeded with v1")
    else:
        print("operation succeeded with v")
    return result                    

divide_by(5,0,0)
divide_by(5,0,1)
divide_by(5,1,0)


print("_______________________________________________")


def demo(a,b):
    try:
        c = ((a+b) // (a-b))

    except ZeroDivisionError:
        print("a/b result in 0")

    else:
        print(c)

# Driver program to test above function
demo(2.0 , 3.0)
demo(3.0 , 3.0) 

value1 = int(input("Enter a first value1: "))
value2 = int(input("Enter a two value2: "))
operater = input("Enter the operater...(+,-,/,*)")

if operater == "+":
    print(value1+value2)

elif operater == "-":
    print(value1-value2)

elif operater == "/":
    print(value1/value2)

elif operater == "*":
    print(value1*value2)
else:
    print("Wrong input program")      
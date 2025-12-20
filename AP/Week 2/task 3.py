task3 = input("Enter the equation: ")
x = task3[0]
operation = task3[1]
num1 = task3[2]
num2 = task3[4]

if x == "x":
    num2 = int(num2)
    num1 = int(num1)
    if operation == "-":
        print(num2+num1)
    else:
        print(num2-num1)
elif num1 == "x":
    num2 = int(num2)
    x = int(x)
    if operation == "-":
        print(x-num2)
    else:
        print(num2-x)
elif num2 == "x":
    num1 = int(num1)
    x = int(x)
    if num2 =="-":
        print(x-num1)
    else:
        print(x+num1)
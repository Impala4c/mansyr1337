n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
o = input("Enter operator (+, -, *, /): ")
if o == '+':
    print ("Your first number: ",n1 ,"Your operation was:",o,"Your second number:",n2,"The result is:",n1+n2)
elif o == '-':
    print ("Your first number: ",n1 ,"Your operation was:",o,"Your second number:",n2,"The result is:",n1-n2)
elif o == '*':
    print ("Your first number: ",n1 ,"Your operation was:",o,"Your second number:",n2,"The result is:",n1*n2)
elif o == '/':
    if n2 != 0:
        print ("Your first number: ",n1 ,"Your operation was:",o,"Your second number:",n2,"The result is:",n1/n2)
    else:
        print("Error: Division by zero is not allowed.")
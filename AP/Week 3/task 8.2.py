def sp(x):
    temp = x[0]
    x[0] = x[-1]
    x[-1]= temp 

size = int(input("Enter the size of your array:"))
a =  []
for i in range(size):
    i = int(input("Enter the values of array:"))
    a.append(i)
print("Og:",a)
sp(a)
print("\nResulting array:", end=" ")
for x in a:
    print(x, end=" ")
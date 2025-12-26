import math
size = int(input("Input how much numbers in arrays you want:"))
a = []
b = []
c = []
for i in range(size):
    i = int(input("numbers for your first array:"))
    a.append(i)
for i in range(size):
    i = int(input("numbers for your second array:"))
    b.append(i)
for i in range(size):
    i = int(input("numbers for your third array:"))
    c.append(i)
if math.fsum(a) > 15 or math.fsum(b) > 15 or math.fsum(c) > 15:
    print("Exceed the number")
else:
    print("Sum of first array:",math.fsum(a))
    print("Sum of second array:",math.fsum(b))
    print("Sum of third array:",math.fsum(c))
    
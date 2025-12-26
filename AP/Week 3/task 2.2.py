rec1 = []
rec2 = []
rec3 = []
for i in range(2):
    i = int(input("The sides of 1 rectangle:"))
    rec1.append(i)
for i in range(2):
    i = int(input("The sides of 2 rectangle:"))
    rec2.append(i)
for i in range(2):
    i = int(input("The sides of 1 rectangle:"))
    rec3.append(i)

area1 = rec1[0] * rec1[1]
area2 = rec2[0] * rec2[1]
area3 = rec3[0] * rec3[1]
print("Area of the first a rectangle is:",area1)
print("Area of the second a rectangle is:",area2)
print("Area of the third a rectangle is:",area3)
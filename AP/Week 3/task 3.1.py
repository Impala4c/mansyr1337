import math

sides = []
for i in range(2):
    i = int(input("Enter the sides of triangle:"))
    sides.append(i)
c = sides[0]*sides[0] + sides[1]*sides[1]
ans = math.sqrt(c)
print(ans)
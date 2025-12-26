import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
d = float(input("Enter side d: "))
diag = float(input("Enter the diagonal: "))
s1 = (a + b + diag) / 2
area1 = math.sqrt(s1 * (s1 - a) * (s1 - b) * (s1 - diag))
s2 = (c + d + diag) / 2
area2 = math.sqrt(s2 * (s2 - c) * (s2 - d) * (s2 - diag))
total_area = area1 + area2

print("Area of the convex quadrilateral:", total_area)

def findGCD(a, b):
    if a == 0:
        return b
    return findGCD(b % a, a)



a = int(input())
b = int(input())
c = int(input())
d = int(input())
s1 = a * d 
s2 = b*c



findGCD(s1,s2)
def findGCD(a, b):
    if a == 0:
        return b
    return findGCD(b % a, a)



a = int(input())
b = int(input())
c = int(input())
d = int(input())
s1 = a*d - c*b
s2 = b*d



print(s1/(findGCD(s1,s2)),s2/(findGCD(s1,s2)))
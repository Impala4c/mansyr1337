def findGCD(a, b):
    if a == 0:
        return b
    return findGCD(b % a, a)


a = int(input("Enter first num:"))
b = int(input("Enter second num:"))
print(findGCD(a,b))
print((a*b)/findGCD(a,b))
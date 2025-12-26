def rect(a,b):
    return a*b
def triangle(a,b):
    return 0.5 * a * b

x = int(input())
y = int(input())
z = int(input())
t = int(input())

print (rect(x,y))
print (triangle(x,y)+triangle(z,t))

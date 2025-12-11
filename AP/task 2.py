a = int(input())
b = int(input())
c = int(input())
max = 0 
min = 0
if a>b and a>c:
    max = a
    if b>c:
        min = c
    else:
        min = b
elif b>a and b>c:
    max = b
    if a>c:
        min = c
    else:
        min = a
elif c>b and c>a:
    max = c
    if b>a:
        min = a
    else:
        min = b
print(max - min)
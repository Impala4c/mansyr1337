x = int(input())
if x > 0:
    a = ""
    if x == 0:
        a="0"
    else:
        t = x
        while t >0:
            o = t %8
            a =  str(o) + a
            t = t//8
    while len(a) < 10:
        a = "0" + a
else:
    print("False")
print(a)
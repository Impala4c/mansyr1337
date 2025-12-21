x = input()
y = input()
if len(x) != len(y):
    print("NO")
else:
    checker = True
    for ch in x:
        if x.count(ch) != y.count(ch):
            checker = False
            break
    if checker == True:
        print("YES")
    else:   
        print("NO")
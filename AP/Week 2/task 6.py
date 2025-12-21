def all_eq(x):
    max = 0
    for i in x:
        if len(i) > max:
            max = len(i)
    
    result = []
    for j in x:
        pos = max - len(j)
        result.append(j + bas * pos)
        
    return result
s = int(input())
bas = input()
a = []
for i in range(s):
    t = input()
    a.append(t)
print(all_eq(a))
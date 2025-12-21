s = set()
x = input()
y = input()
dlina = len(y)
dlina1= y+y
counter = 0
for i in range(dlina):
    s.add(dlina1[i:dlina+i])
for j in range(len(x)-dlina+1):
    if x[j:dlina+j] in s:
        counter += 1
print(counter)
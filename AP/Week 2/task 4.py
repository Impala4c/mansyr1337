a, b = map(int, input().split())
st = input()
w = []
for i in range(a - b + 1):
    p = st[i:i+b]
    if p not in w:
        w.append(p)

print(len(w))
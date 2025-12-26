c = 0 
a = ">>-->" 
b = "<--<<" 
st = str(input("Enter the string: ")) 
for i in range(len(st)): 
    if st[i:i+5] == a or st[i:i+5] == b: 
        c += 1 
print("Number of arrows found:", c)
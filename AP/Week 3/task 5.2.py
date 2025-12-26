div = []
n = int(input("Enter the number:"))
x = n  
i = 1
while x > 0:
    if n%i==0:
        div.append(i)
    x -=1
    i +=1
print(div)
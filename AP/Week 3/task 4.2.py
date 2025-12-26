def circle(x,y,a,b,r):
    return (x - a)**2+(y-b)**2 < r**2
a = int(input())
b = int(input())
r = int(input())
points1 = []
points2 = []
point = []
p = int(input("how many points do you want to check?:"))
count = 0
for i in range(p):
    i = int(input(f"add point of x{i+1}:"))
    points1.append(i)
for i in range(p):
    i = int(input(f"add point of y{i+1}:"))
    points2.append(i)
for i in range(p):
    if circle(points1[i],points2[i],a,b,r):
        count+=1
print("The points in circle",count)
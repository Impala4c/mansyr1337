def sum(x):
    if x == 0:
        return 0
    else:
        return x+sum(x-1)
num = int(input("Input your number:"))
print(sum(num))



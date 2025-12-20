A = "ABCEHKMOPTXY"

line = int(input())

for i in range(line):
    st = input()
    f = True
    if len(st) != 6:
        f = False
    else:
        if st[0] not in A:
            f = False
        if not st[1].isdigit() or not st[2].isdigit() or not st[3].isdigit():
            f = False
        if st[4] not in A or st[5] not in A:
            f = False
    if f == True:
        print("Yes")
    else:
        print("No")

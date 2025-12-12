w = str(input("Enter a word: "))
n = int(input("Enter a number: "))
num = n 
init = 0
while num > 0:
    for n in range(len(w)):
        print(w[init])
    init += 1
    num-=1
    

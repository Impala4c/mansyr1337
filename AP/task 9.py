x = int(input())
sum1=0
sum2=0
sum1= (x//100000)+(x//10000%10)+(x//1000%10)
sum2= (x//100%10)+(x//10%10)+(x%10)
if sum1==sum2:
    print("Lucky ticket")
else:
    print("NOT lucky ticket")
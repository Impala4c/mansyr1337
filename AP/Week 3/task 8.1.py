n = int(input("Enter n: "))

result = []

for num in range(1, n + 1):
    temp = num
    valid = True

    while temp > 0:
        digit = temp % 10
        if digit == 0 or num % digit != 0:
            valid = False
            break
        temp //= 10

    if valid:
        result.append(num)

print("Numbers:", result)

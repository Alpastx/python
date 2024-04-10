def sum(N):
    sum = 0
    while N > 0:
        digit = N % 10
        sum += digit
        N = N // 10
    return sum
N = int(input("Enter the number: "))
print(sum(N))
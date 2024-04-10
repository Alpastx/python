def fact(N):
    if N == 0 or N == 1:
        return 1
    else:   
        fact = 1
        for i in range(2,N+1):
            fact *= i
        return fact
N = int(input("Enter the number: "))
print(fact(N))
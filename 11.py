def fibo(i):
    if i <= 1:
        return i
    else:
        return fibo(i - 1) + fibo(i - 2)
N = int(input("Enter the number of terms: "))
for i in range(N):
    print(fibo(i))
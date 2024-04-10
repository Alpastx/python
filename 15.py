def pali(N):
    N = str(N)
    if N == N[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"
N = int(input("Enter the number: "))
print(pali(N))
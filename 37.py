def is_prime(number):
    if number <= 1:
        return False
    return all(number % i != 0 for i in range(2, int(number ** 0.5) + 1))

# Example usage:
num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

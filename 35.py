def counter(t):
    upper = sum(1 for i in t if i.isupper())
    lower = sum(1 for i in t if i.islower())
    return upper, lower
t = input("Enter a string: ")
print("Uppercase and Lowercase count:", counter(t))
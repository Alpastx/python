def trymax(n1,n2,n3):
    if n1 > n2:
        if n1 > n3:
            return n1
        else:
            return n3
    else:
        if n2 > n3:
            return n2
        else:
            return n3
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
print("the max number is :",trymax(n1,n2,n3))

#or

def maxed(n1,n2,n3):
    return max(n1,n2,n3)
print("the max number is :",maxed(n1,n2,n3))
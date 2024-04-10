def mul(l1):
    res =1 
    for item in l1:
        res *= item
    return res
N =[int(x) for x in input("Enter space-separated numbers: ").split()]
print(mul(N))
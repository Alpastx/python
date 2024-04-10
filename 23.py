def minmax(t1):
    return (min(t1), max(t1))
N =[int(x) for x in input("Enter space-separated numbers: ").split()]
print(minmax(N))
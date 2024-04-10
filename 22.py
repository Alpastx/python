def checkeven(l1):
    return [item for item in l1 if item%2 == 0]
l1 = [int(x) for x in input("Enter space-separated numbers: ").split()]
print(checkeven(l1))
      
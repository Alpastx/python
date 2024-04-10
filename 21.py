def common(l1,l2):
    return list(set(l1) & set(l2))
l1 = input("Enter space-separated elements of the first list: ").split()
l2 = input("Enter space-separated elements of the second list: ").split()
print(common(l1,l2))
    
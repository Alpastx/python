s1 = {int(x) for x in input("Enter space-separated numbers for the set: ").split()}
s1.add(20)
s1.add(30)
s1.add(40)
print("Before removal:",s1)
rem = int(input("Enter the element to remove: "))
s1.remove(rem)
print("After removal:",s1)
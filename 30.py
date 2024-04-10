d1 = {'a': 5, 'b': 3, 'c': 8, 'd': 1, 'e': 10}

Asorted = sorted(d1.items(), key=lambda x: x[1])
Dsorted = dict(sorted(d1.items(), key=lambda x: x[1], reverse=True))

print("Dictionary in ascending order by value: ", Asorted)
print("Dictionary in descending order by value: ", Dsorted)
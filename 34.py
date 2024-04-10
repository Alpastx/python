
data = {"a": 10, "b": 50, "c": 30, "d": 70, "e": 40}
highest_values = sorted(data.values(), reverse=True)[:3]
print("Highest 3 values in the dictionary:")
for value in highest_values:
    print(value)

data = {"V": "S001", "V": "S002", "VI": "S001", "VI": "S005", "VII":"S005", "V":"S009","VIII":"S007"}

unique_values = set(data.values())
print("Unique values in the dictionary:")
for value in unique_values:
    print(value)
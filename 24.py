def rep(tup):
    repeated_items = set()
    unique_items = set()
    for item in tup:
        if item in unique_items:
            repeated_items.add(item)
        else:
            unique_items.add(item)
    
    return repeated_items

input_tuple = tuple(input("Enter space-separated items for the tuple: ").split())
repeated_items = find_repeated_items(input_tuple)
print("Repeated items in the tuple:", repeated_items)

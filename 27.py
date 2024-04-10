def set_operations(set1, set2):

    intersection = set1.intersection(set2)
    print("Intersection of sets:", intersection)
    union = set1.union(set2)
    print("Union of sets:", union)

    difference1 = set1 - set2
    print("Set difference (Set1 - Set2):", difference1)

    difference2 = set2 - set1
    print("Set difference (Set2 - Set1):", difference2)

    symmetric_difference = set1.symmetric_difference(set2)
    print("Symmetric difference of sets:", symmetric_difference)

    set1.clear()
    print("Set1 after clearing:", set1)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set_operations(set1, set2)

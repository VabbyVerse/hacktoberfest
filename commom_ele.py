list_a = [1, 2, 3, 4, 5, 6]
list_b = [4, 5, 6, 7, 8, 9]

# Convert lists to sets for fast operations
set_a = set(list_a)
set_b = set(list_b)

# Intersection (Common elements)
common = set_a.intersection(set_b)
# Union (All unique elements)
all_elements = set_a.union(set_b)
# Difference (Elements in A but not B)
only_in_a = set_a.difference(set_b)

print(f"List A: {list_a}")
print(f"List B: {list_b}")
print(f"Common Elements: {list(common)}")
print(f"All Unique Elements: {list(all_elements)}")
print(f"Only in A: {list(only_in_a)}")

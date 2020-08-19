# List Datatype (Mutable)

a = [10, 3, 89, 90, 67, 3.14, 'pineapple', True, 3+5j, [1, 2, 3]]

# Append into list
a.append(100)

# Insert value at index
a.insert(2, 32)

# Remove value
a.remove(3)

print(a)

# Indexing
print(a[4])

# Slicing
# syntax: list_variable[start_index:last_index:steps]
print(a[2:4])
print(a[2:])
print(a[::2])

# Delete entire list
del a

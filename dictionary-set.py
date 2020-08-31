'''
Dictionary & Set
  - Dictionary  {}
      Keys should be of type immutable

Previous Classes:
  - List   []
  - Tuple  ()
'''

# Fast for insertion, deletion and traversing
# Time-space complexity
# It is measure in Big 'O' notation
# O(1), O(1), O(1)
d = {100: 3.14, 'fruit': 'apple', 'number': 100, 12: 'apple'}
d['game'] = 'football'
d.pop('fruit')  # Remove key, value pair from dict
print(d)

s1 = {1, 2, 3, 5, 7, 9, 10}
s2 = {2, 4, 6, 8, 10}

print(s1)
print(s2)

# Set Union
print(s1 | s2)

# Set Intersection
print(s1 & s2)

# Set Difference
print(s1 - s2)
print(s2 - s1)

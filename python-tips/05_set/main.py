import time
import random

some_list = []
for i in range(10000):
    some_list.append(random.choice('abcdefghijklmnopqrstuvwxyz'))

# Inefficient way
duplicates = []
start_inefficient = time.time()
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
end_inefficient = time.time()
print(sorted(duplicates))

# Efficient way

start_efficient = time.time()
duplicates = set([x for x in some_list if some_list.count(x) > 1])
end_efficient = time.time()
print(sorted(duplicates))

print("Time taken by inefficient method: ", end_inefficient - start_inefficient)
print("Time taken by efficient method: ", end_efficient - start_efficient)

# Intersection
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.intersection(valid))
# Output: set(['red'])

# Difference
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.difference(valid))
# Output: set(['brown'])

# Union
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.union(valid))
# Output: set(['blue', 'green', 'black', 'brown', 'red', 'yellow'])

# Symmetric Difference
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.symmetric_difference(valid))
# Output: set(['blue', 'green', 'black', 'brown', 'yellow'])

# Subset
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.issubset(valid))
# Output: False

# Superset
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.issuperset(valid))
# Output: False

# Disjoint
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.isdisjoint(valid))
# Output: False

a_set = {'red', 'blue', 'green'}
print(type(a_set))
# Output: <type 'set'>

# Sets

my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set.add(6)
print(my_set)

my_set.remove(2)
print(my_set)

#Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set_union = set1.union(set2) # This combines both sets and remove the duplicates
print(set_union)

#Intersection
set_intersection = set1.intersection(set2) # This returns only the elements that are present in both sets
print(set_intersection)

#Difference
set_difference = set1.difference(set2) # This returns the elements that are in set1 but not in set2
print(set_difference)
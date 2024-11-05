def intersect_dictionaries(d1, d2):
    common_keys = d1.keys() & d2.keys() #finding the common with respect to keys
    d3 = {key: d1[key] for key in common_keys} #using dictionary comprehension to create a new dictionary with the common keys
    return d3

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 4, 'c': 3, 'd': 5}
print(intersect_dictionaries(d1, d2))

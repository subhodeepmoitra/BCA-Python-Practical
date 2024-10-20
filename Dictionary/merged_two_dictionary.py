def merged_dictionary(d1,d2):
    dm = d1.copy()
    for key, value in d2.items():
        if key in dm:
            dm[key] += value
        else:
            dm[key] = value
    return dm

d1 = {'a':1,
      'b':2,
      'c':3}
d2 = {'b':3,
      'c':1,
      'd':4}
result = merged_dictionary(d1,d2)
print(f"The merged dictionary is = {result}")
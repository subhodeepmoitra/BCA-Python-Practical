def merged_dictionary(d1,d2):
    dm = d1.copy()
    for key, value in d2.items():
        if key in dm:
            dm[key] += value
        else:
            dm[key] = value
    return dm

d1 = {'uts':1,
      'ntes':2,
      'pts':3}
d2 = {'ntes':3,
      'pts':1,
      'tts':4}
result = merged_dictionary(d1,d2)
print(f"The merged dictionary is = {result}")
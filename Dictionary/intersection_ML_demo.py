def common_key(ANN,LSTM):
    common_keys = ANN.keys() & LSTM.keys()
    common = {key: (ANN[key], LSTM[key]) for key in common_keys}
    return common

def common_value(ANN, LSTM):
    common_values = set(ANN.values()) & set(LSTM.values()) #finding the unique values
    common = {} #a new dictionary for storing the common values and their respective keys
    for value in common_values:
        ann_keys = [key for key, val in ANN.items() if val == value] # ANN list -> is value is true for value in line 9
        lstm_keys = [key for key, val in LSTM.items() if val == value] # ANN list -> is value is true for value in line 9
        common[value] = (ann_keys, lstm_keys) # common dictionary line 8 -> key = value && values = list of the ann and lstm keys
    return common


ANN = {
    'mse':0.92,
    'rmse':0.89,
    'mae':0.85,
    'r2':0.87
}

LSTM = {
    'mse':0.90,
    'rmse':0.91,
    'mae':0.88,
    'r2':0.89
}

common = common_key(ANN,LSTM)
commonValue = common_value(ANN,LSTM)
print(f"Common by keys: {common}")
print(f"Common by values: {commonValue}")
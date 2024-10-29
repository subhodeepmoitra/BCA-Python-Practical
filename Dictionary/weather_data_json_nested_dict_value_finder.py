def getValue(nested_dict, keys):
    current_value = nested_dict
    for key in keys:  # Traversing through each key in the list of keys
        current_value = current_value[key]  # Updating the current value to be the value associated with the present key
    return current_value

def extractKeys(nested_dict):
    keys = []
    def traverse(d):
        for key, value in d.items():  # Extracting the key-value pairs from the dictionary
            keys.append(key)
            if isinstance(value, dict):  # If the value is a nested dictionary, traverse it
                traverse(value)
    traverse(nested_dict)
    return keys

weather_data = {
    "location": {
        "city": "Alipore, Kolkata",
        "country": "India",
        "coordinates": {
            "latitude": 40.7128,
            "longitude": -74.0060
        }
    },
    "current": {
        "temperature": 22,
        "condition": "Sunny",
        "humidity": 56,
        "wind": {
            "speed": 5,
            "direction": "NE"
        }
    },
    "forecast": {
        "daily": [
            {"day": "Monday", "high": 25, "low": 18, "condition": "Partly cloudy"},
            {"day": "Tuesday", "high": 23, "low": 17, "condition": "Rain"},
            {"day": "Wednesday", "high": 24, "low": 19, "condition": "Sunny"}
        ]
    }
}

keys = extractKeys(weather_data) #key extraction

# Accessing specific values from the nested weather data
temperature_key = ["current", "temperature"] #from current dictionary use temperature key
condition_key = ["current", "condition"] #from current dictionary use condition key
city_key = ["location", "city"] #from location dictionary use city key
coordinate_key = ["location","coordinates"]

temperature = getValue(weather_data, temperature_key)  # Extract current temperature
condition = getValue(weather_data, condition_key)  # Extract current weather condition
city = getValue(weather_data, city_key)  # Extract city name
coordinates = getValue(weather_data, coordinate_key) #coordinates extraction

# Displaying the extracted information
print(f"Current weather in {city}, coordinates {coordinates}: {temperature}°C, {condition}.")

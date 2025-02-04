import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

# Python Question 1: Data Aggregation
# Write a Python function that takes a list of dictionaries representing energy consumption data and other metadata that can be aggregated (i.e. int or float values)
# and returns a dictionary with the total consumption and other metadata for each device.

def aggregate_metadata(data):
    result = {}
    for entry in data:
        # ensure device_id exists for each row of data list
        if 'device_id' in entry:
            device_id =  entry['device_id']
            # initialize current device_id as a key with values as a dictionary in result dictionary if it doesnt exist
            if device_id not in result:
                result[device_id] = {}
            
            for key, value in entry.items():
                if key == 'device_id':
                    continue
                # check if value is numeric
                if isinstance(value, (int, float)):
                    # aggregate numeric value
                    if key in result[device_id]:
                        result[device_id][key] += value
                    else:
                        result[device_id][key] = value
    return result

# Example usage
data = [
    {'device_id': 1, 'consumption': 10},
    {'device_id': 2, 'consumption': 15},
    {'device_id': 1, 'consumption': 5},
]
print(aggregate_metadata (data))  # Output: {1: 15, 2: 15}

# Explanation:
# 1. Initialize an empty dictionary `result` to store the total consumption for each device.
# 2. Iterate through each entry in the input list `data`.
# 3. For each entry, extract the `device_id` and `consumption`.
# 4. If the `device_id` is already in the `result` dictionary, add the `consumption` to the existing value.
# 5. If the `device_id` is not in the `result` dictionary, add a new key-value pair with the `device_id` and `consumption`.
# 6. Return the `result` dictionary.


# Python Question 2: Anomaly Detection
# Write a Python function that takes a list of energy consumption readings and detects anomalies
# where the consumption is more than double the average of the previous readings.

def detect_anomalies(readings):
    anomalies = []
    for i in range(1, len(readings)):
        avg_previous = sum(readings[:i]) / i
        if readings[i] > 2 * avg_previous:
            anomalies.append((i, readings[i]))
    return anomalies

# Example usage
readings = [10, 12, 15, 40, 18, 20]
print(detect_anomalies(readings))  # Output: [(3, 40)]

# Explanation:
# 1. Initialize an empty list `anomalies` to store the indices and values of detected anomalies.
# 2. Iterate through the `readings` list starting from the second element (index 1).
# 3. For each reading, calculate the average of all previous readings.
# 4. If the current reading is more than double the average of the previous readings, add the index and value to the `anomalies` list.
# 5. Return the `anomalies` list.


# Python Question 3: Rolling Average Calculation
# Write a Python function that calculates the rolling average of energy consumption over a specified window size.

def rolling_average(data, window_size):
    if window_size > len(data):
        return []
    averages = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        averages.append(sum(window) / window_size)
    return averages

# Example usage
data = [10, 12, 15, 20, 18, 20]
window_size = 3
print(rolling_average(data, window_size))  # Output: [12.33, 15.67, 17.67, 19.33]

# Explanation:
# 1. Check if the `window_size` is greater than the length of the `data` list. If so, return an empty list.
# 2. Initialize an empty list `averages` to store the rolling averages.
# 3. Iterate through the `data` list, creating windows of the specified `window_size`.
# 4. For each window, calculate the average and append it to the `averages` list.
# 5. Return the `averages` list.


# Python Question 4: Data Normalization
# Write a Python function that normalizes a list of energy consumption values to a range of 0 to 1.

def normalize(data):
    min_val = min(data)
    max_val = max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Example usage
data = [10, 12, 15, 20, 18, 20]
print(normalize(data))  # Output: [0.0, 0.2, 0.5, 1.0, 0.8, 1.0]

# Explanation:
# 1. Find the minimum value `min_val` in the `data` list.
# 2. Find the maximum value `max_val` in the `data` list.
# 3. Normalize each value in the `data` list to a range of 0 to 1 using the formula `(x - min_val) / (max_val - min_val)`.
# 4. Return the list of normalized values.


# Python Question 5: Time Series Decomposition
# Write a Python function that decomposes a time series of energy consumption into trend, seasonal, and residual components using the `statsmodels` library.

def decompose_time_series(data, freq):
    series = pd.Series(data)
    decomposition = seasonal_decompose(series, model='additive', period=freq)
    return decomposition.trend, decomposition.seasonal, decomposition.resid

# Example usage
data = [10, 12, 15, 20, 18, 20, 22, 24, 25, 30, 28, 30]
trend, seasonal, resid = decompose_time_series(data, freq=4)
print("Trend:", trend)
print("Seasonal:", seasonal)
print("Residual:", resid)

# Explanation:
# 1. Convert the input `data` list to a Pandas Series.
# 2. Use the `seasonal_decompose` function from the `statsmodels` library to decompose the time series into trend, seasonal, and residual components.
# 3. The `model='additive'` parameter specifies that the decomposition model is additive.
# 4. The `period=freq` parameter specifies the frequency of the seasonal component.
# 5. Return the trend, seasonal, and residual components.
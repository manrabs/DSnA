# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key 'key' with the value 'value' at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

# Example 1:
# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]

class TimeMap:

    def __init__(self):
        self.store = {} #key = string, value = [list of [value, timestamp]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, []) # returns value list if match found or empty list if not available

        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + (r - l) // 2)
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res


if __name__ == '__main__':
    obj = TimeMap()
    obj.set("f","bar",2)
    print(obj.get("f",2))
    print(obj.get("f", 3))
    bar2 = obj.set('f', 'bar2', 4)
    bar3 = obj.set('f', 'bar2', 5)
    print(obj.get('g', 6))

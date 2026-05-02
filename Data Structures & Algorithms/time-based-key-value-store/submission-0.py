"""
REVISION NOTES - Time Based Key-Value Store:
• HashMap + binary search design for time-based storage
• Store: key -> list of [value, timestamp] pairs (sorted by timestamp)
• Set: append [value, timestamp] to key's list (timestamps are increasing)
• Get: binary search to find largest timestamp ≤ given timestamp
• Key insight: use binary search on timestamps for efficient retrieval
• Time: Set O(1), Get O(log n), Space: O(n) where n is total entries
"""

class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key,[])

        l,r = 0, len(values)-1
        while l <= r:
            m = (l+r)//2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return res

        

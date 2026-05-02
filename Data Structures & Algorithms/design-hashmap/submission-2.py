"""
REVISION NOTES - Design Hashmap:
- Use array with direct indexing for simple implementation
- Handle collisions with chaining or open addressing
- Initialize with default value (-1 for not found)
- All operations should be O(1) average case
- Space: O(capacity)
"""

class MyHashMap:

    def __init__(self):
        self.data =  [-1] * 1000001
        

    def put(self, key: int, value: int) -> None:
        self.data[key] = value
        

    def get(self, key: int) -> int:
        return self.data[key]
        

    def remove(self, key: int) -> None:
        self.data[key] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
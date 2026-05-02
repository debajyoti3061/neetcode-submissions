"""
REVISION NOTES - Design Hashset:
- Use array or list to store elements
- For add: check if exists before adding
- For remove: check if exists before removing
- For contains: linear search or use hash function
- Time: O(1) average with proper hashing, Space: O(n)
"""

class MyHashSet:

    def __init__(self):
        self.data = []
        

    def add(self, key: int) -> None:
        if key not in self.data:
            self.data.append(key)

    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)
        

    def contains(self, key: int) -> bool:
        return key in self.data
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
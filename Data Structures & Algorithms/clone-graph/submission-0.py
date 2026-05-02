"""
REVISION NOTES - Clone Graph:
- Use DFS with hashmap to track original to clone mapping
- For each node, create clone and recursively clone neighbors
- Use hashmap to avoid infinite loops and duplicate clones
- Return clone of starting node
- Time: O(V+E), Space: O(V)
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
            
        return dfs(node) if node else None
        
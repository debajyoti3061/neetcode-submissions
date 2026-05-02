"""
REVISION NOTES - Valid Tree:
• DFS approach to check if graph forms a valid tree
• Valid tree conditions: connected + no cycles + exactly n-1 edges
• Build adjacency list from edges, then DFS from node 0
• Track visited nodes and previous node to avoid going back
• If we visit an already visited node (not previous), there's a cycle
• After DFS, check if all nodes were visited (connectivity)
• Time: O(V + E), Space: O(V + E)
"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adj ={i: [] for i in range(n)}
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        visited = set()
        
        def dfs(i,prev):
            if i in visited:
                return False
            visited.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j,i):
                    return False
            return True
        
        return dfs(0,-1) and len(visited) == n

        
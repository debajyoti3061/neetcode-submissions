"""
REVISION NOTES - Count Connected Components:
- Use DFS or Union-Find to count components
- For each unvisited node, start DFS and mark all reachable nodes
- Increment component count for each DFS start
- Use adjacency list for graph representation
- Time: O(V+E), Space: O(V+E)
"""

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        visited = [False] * n

        def dfs(node):
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        res = 0
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                res += 1
            
        return res
        
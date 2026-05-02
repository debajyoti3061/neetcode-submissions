"""
REVISION NOTES - Course Schedule:
- Model as directed graph, detect cycles using DFS
- Use three states: unvisited, visiting, visited
- If we reach a visiting node, cycle detected
- Mark nodes as visited after processing all neighbors
- Time: O(V+E), Space: O(V)
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        visitSet = set()
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            preMap[crs] = []
            visitSet.remove(crs)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        
"""
REVISION NOTES - Combinations:
- Use backtracking to generate all k-element combinations
- Build combination incrementally, backtrack when complete
- Use start index to avoid duplicate combinations
- Add to result when combination size reaches k
- Time: O(C(n,k)), Space: O(k)
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(start,comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            
            for i in range(start,n+1):
                comb.append(i)
                dfs(i+1,comb)
                comb.pop()
        
        dfs(1,[])
        return res

"""
REVISION NOTES - Subsets:
- Use backtracking to generate all possible subsets
- For each element, choose to include or exclude it
- Build subset incrementally and backtrack
- Add current subset to result at each recursive call
- Time: O(2^n), Space: O(n)
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
            return res

        dfs(0)
        return res        
"""
REVISION NOTES - Subsets Ii:
- Sort array first to handle duplicates
- Use backtracking similar to subsets
- Skip duplicate elements at same recursion level
- Only process duplicate if previous same element was included
- Time: O(2^n), Space: O(n)
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i,comb):
            if i == len(nums):
                res.append(comb.copy())
                return
            
            
            comb.append(nums[i])
            dfs(i+1,comb)
            comb.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            dfs(i+1,comb)
        nums.sort()
        dfs(0,[])
        return res

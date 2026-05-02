"""
REVISION NOTES - Permutations:
- Use backtracking with visited array or by swapping
- Build permutation one element at a time
- Mark elements as used, backtrack by unmarking
- Add complete permutation to result
- Time: O(n!), Space: O(n)
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def dfs(comb):
            if len(comb) == len(nums):
                res.append(comb.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                # choose
                used[i] = True
                comb.append(nums[i])

                dfs(comb)

                # backtrack
                comb.pop()
                used[i] = False
        
        dfs([])
        return res
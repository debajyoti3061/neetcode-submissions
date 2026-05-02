"""
REVISION NOTES - Combination Target Sum:
- Use backtracking with remaining target sum
- For each candidate, subtract from target and recurse
- Allow reusing same candidate (start index doesn't change)
- Backtrack by removing last added candidate
- Time: O(2^t) where t is target, Space: O(t)
"""

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(temp_list, remain, start):
            if remain < 0:
                return
            elif remain == 0:
                result.append(list(temp_list))
                return
            else:
                for i in range(start, len(nums)):
                    temp_list.append(nums[i])
                    dfs(temp_list, remain - nums[i], i)  # FIXED
                    temp_list.pop()

        dfs([], target, 0)
        return result
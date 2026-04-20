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
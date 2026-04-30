class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        nums.sort()

        def dfs(comb):
            if len(comb) == len(nums):
                res.append(comb.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                # skip duplicates
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
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
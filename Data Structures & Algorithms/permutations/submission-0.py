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
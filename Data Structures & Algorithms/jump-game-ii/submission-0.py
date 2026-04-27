class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, curEnd, curFurthest = 0, 0 , 0
        for i in range(len(nums)-1):
            curFurthest = max(curFurthest, i+nums[i])
            if i == curEnd:
                jumps += 1
                curEnd = curFurthest
        
        return jumps
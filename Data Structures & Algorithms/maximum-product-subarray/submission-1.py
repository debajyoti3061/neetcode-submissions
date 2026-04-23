class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1 , 1
        res = nums[0]
        for num in nums:
            
            tmp = curMax * num
            curMax = max(curMax * num,curMin * num, num)
            curMin = min(tmp,curMin * num, num)
            res = max(res,curMax)
        return res
        
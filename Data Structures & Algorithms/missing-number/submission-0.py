class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for num in nums:
            res += num
        total = n * (n+1)/2
        return int(total-res)
        
        
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = [False] * len(nums)
        for num in nums:
            if num > 0 and num <= len(nums):
                seen[num-1] = True
        for i in range(1,len(seen)+1):
            if not seen[i-1]:
                return i
        return len(nums)+1

        
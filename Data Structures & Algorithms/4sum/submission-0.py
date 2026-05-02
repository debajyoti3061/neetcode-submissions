"""
REVISION NOTES - 4Sum:
• Sort array first to enable two-pointer technique and handle duplicates
• Use recursive kSum approach: reduce 4Sum to 3Sum to 2Sum
• Base case is 2Sum using two pointers from both ends
• Skip duplicates at each level to avoid duplicate quadruplets
• Time: O(n³), Space: O(1) excluding output
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        return self.kSum(nums, target, 4, 0)

    def kSum(self, nums: List[int], target: int, k: int, index: int):
        res = []
        
        # Not enough numbers left
        if index >= len(nums):
            return res

        # Base case: 2Sum (two pointers)
        if k == 2:
            i, j = index, len(nums) - 1
            while i < j:
                curr_sum = nums[i] + nums[j]
                if curr_sum == target:
                    res.append([nums[i], nums[j]])
                    
                    # Skip duplicates
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                        
                    i += 1
                    j -= 1
                elif curr_sum < target:
                    i += 1
                else:
                    j -= 1
        else:
            for i in range(index, len(nums) - k + 1):
                
                # Skip duplicates
                if i > index and nums[i] == nums[i - 1]:
                    continue
                
                subsets = self.kSum(nums, target - nums[i], k - 1, i + 1)
                
                for subset in subsets:
                    res.append([nums[i]] + subset)
        
        return res

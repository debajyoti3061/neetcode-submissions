"""
REVISION NOTES - Rotate Array:
• Three-step reversal approach for O(1) space rotation
• Step 1: Reverse first n-k elements
• Step 2: Reverse last k elements
• Step 3: Reverse entire array
• Use k %= n to handle cases where k > n
• This achieves right rotation by k positions in-place
• Time: O(n), Space: O(1)
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.reverse(nums,0,n-k-1)  
        self.reverse(nums,n-k,n-1)
        self.reverse(nums,0,n-1)
    
    def reverse(self,nums: List[int], start: int, end: int):
        while start < end:
            nums[start] , nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


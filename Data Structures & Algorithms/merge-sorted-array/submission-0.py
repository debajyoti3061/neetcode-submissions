"""
REVISION NOTES - Merge Sorted Array:
• Merge from the end to avoid overwriting elements in nums1
• Use three pointers: last (write position), m-1 (nums1 read), n-1 (nums2 read)
• Compare elements from end of both arrays, place larger one at 'last' position
• Continue until one array is exhausted
• If nums2 has remaining elements, copy them to nums1
• Time: O(m+n), Space: O(1)
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                last -= 1
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                last -= 1
                n -= 1
        
        while n > 0:
            nums1[last] = nums2[n-1]
            last -= 1
            n -= 1
        
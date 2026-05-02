"""
REVISION NOTES - Sort An Array:
• Merge sort implementation with divide-and-conquer approach
• Recursively divide array into halves until single elements
• Merge sorted halves back together in sorted order
• Use temporary arrays for left and right subarrays during merge
• Three-pointer technique: one for result position, two for subarray positions
• Handle remaining elements from either subarray after main merge
• Time: O(n log n), Space: O(n)
"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        def mergeSort(nums, l, r):
            if l >= r:
                return
            m = (l+r) //2
            mergeSort(nums,l,m)
            mergeSort(nums,m+1,r)
            merge(nums, l,m,r)

        def merge(nums, L, M, R):
            left, right = nums[L:M+1] , nums[M+1:R+1]
            i, j, k = L, 0, 0
            while j < len(left) and k < len(right):
                if left[j] <= right[k] :
                    nums[i] = left[j]
                    j += 1
                else:
                    nums[i] = right[k]
                    k += 1
                i += 1

            while j < len(left) :
                nums[i] = left[j]
                j += 1
                i += 1
            
            while k < len(right) :
                nums[i] = right[k]
                k += 1
                i += 1
        
        mergeSort(nums,0, len(nums)-1)
        return nums

        
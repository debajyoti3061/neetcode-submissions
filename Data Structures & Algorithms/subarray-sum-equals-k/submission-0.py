"""
REVISION NOTES - Subarray Sum Equals K:
• Prefix sum + hashmap approach to find subarrays with sum = k
• Key insight: if current_sum - k exists in map, we found valid subarray(s)
• Track frequency of each prefix sum to handle multiple occurrences
• Initialize map with {0: 1} to handle subarrays starting from index 0
• For each element: check if (current_sum - k) exists, then update map
• Time: O(n), Space: O(n)
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_sums = {0: 1} # Initialize with 0:1 to handle subarrays starting from index 0

        for num in nums:
            current_sum += num
        # If (current_sum - k) exists in map, add its frequency
            if (current_sum - k) in prefix_sums:
                count += prefix_sums[current_sum - k]
        # Update map with current_sum
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
        
        return count
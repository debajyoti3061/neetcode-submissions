"""
REVISION NOTES - Majority Element II:
• Find all elements that appear more than n/3 times
• Use Counter to count frequency of each element
• Check each element's count against threshold n//3
• At most 2 elements can appear more than n/3 times
• Alternative: Boyer-Moore generalized voting algorithm for O(1) space
• Time: O(n), Space: O(n)
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []

        for i in count.keys():
            if count[i] > len(nums)//3:
                res.append(i)
        return res
        
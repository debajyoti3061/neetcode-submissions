"""
REVISION NOTES - Single Number:
- Use XOR operation: a XOR a = 0, a XOR 0 = a
- XOR all numbers together
- Duplicate numbers cancel out, leaving only single number
- Works because XOR is commutative and associative
- Time: O(n), Space: O(1)
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            answer ^= num
        return answer

        
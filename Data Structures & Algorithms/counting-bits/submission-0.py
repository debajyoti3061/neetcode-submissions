"""
REVISION NOTES - Counting Bits:
- Use dynamic programming with bit manipulation
- dp[i] = dp[i >> 1] + (i & 1)
- Right shift removes last bit, i & 1 checks if last bit is set
- Build up from smaller numbers
- Time: O(n), Space: O(n)
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n+1):
            temp = 0
            while (num):
                temp += num%2
                num = num >> 1
            res.append(temp)
        return res

                    
        
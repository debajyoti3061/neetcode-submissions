"""
REVISION NOTES - Combinations Of A Phone Number:
- Use backtracking with digit-to-letters mapping
- For each digit, try all possible letters
- Build string incrementally, backtrack when complete
- Add to result when string length equals digits length
- Time: O(4^n), Space: O(n)
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        map = {"2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"}

        def backtrack(i,cur):
            if len(cur) == len(digits):
                res.append(cur)
                return
            for c in map[digits[i]]:
                backtrack(i+1,cur+c)
        if digits:
            backtrack(0,"")
        return res
        
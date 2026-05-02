"""
REVISION NOTES - Palindrome Partitioning:
• Backtracking to generate all possible palindrome partitions
• For each position, try all possible substrings starting from that position
• Check if substring is palindrome before adding to current partition
• When reach end of string, add current partition to results
• Backtrack by removing last added substring and trying next possibility
• Time: O(n * 2^n), Space: O(n)
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
            for j in range (i,len(s)):
                if self.isPalindrome(s,i,j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res
        
    def isPalindrome(self,s,i,j):
        while i < j:
            if s[i] != s[j]:
                return False
            i,j = i+1, j-1
        return True
        
        
        
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.countPal(s,i,i)
            res += self.countPal(s,i,i+1)
        return res

    def countPal(self,s,i,j):
        res = 0
        while i >= 0 and j < len(s) and s[i]==s[j]:
            res += 1
            i -= 1
            j += 1
        return res
        
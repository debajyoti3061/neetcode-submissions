"""
REVISION NOTES - Minimum Window With Characters:
- Use two hashmaps: one for target characters, one for window
- Expand window until all target characters included
- Then shrink from left while maintaining validity
- Track minimum valid window found
- Time: O(n), Space: O(m) where m is target string length
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" :
            return ""
        countT, window = {}, {}

        for i in t:
            countT[i] = 1 + countT.get(i,0)
        have, need = 0, len(countT)
        res, resLen = [-1,-1] , float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1+ window.get(c,0)

            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r= res
        return s[l:r+1] if resLen != float("infinity") else ""
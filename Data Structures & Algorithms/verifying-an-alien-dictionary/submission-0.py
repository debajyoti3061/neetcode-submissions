"""
REVISION NOTES - Verifying an Alien Dictionary:
• Create mapping from alien characters to their order indices
• Compare adjacent words character by character
• For each pair of words, find first differing character
• If w1[j] != w2[j], check if w2[j] comes before w1[j] in alien order
• Special case: if w1 is prefix of w2 but longer, return False
• If all character comparisons pass, words are in correct order
• Time: O(N*M) where N is number of words, M is average word length, Space: O(1)
"""

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        map = {j:i for i,j in enumerate(order)}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]

            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if w1[j] != w2[j]:
                    if map[w2[j]] < map[w1[j]]:
                        return False
                    break
        return True
        
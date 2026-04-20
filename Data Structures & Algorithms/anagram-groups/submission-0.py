class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:
            charArray = [a for a in s]
            charArray.sort()
            tempString = ('').join(charArray)
            if tempString not in map:
                map[tempString] = []
            map[tempString].append(s)
        return list(map.values())
        
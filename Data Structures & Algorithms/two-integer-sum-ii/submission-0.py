class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = defaultdict(int)
        for i in range(len(numbers)):
            temp = target-numbers[i]
            if temp in map.keys():
                return [map[temp],i+1]
            map[numbers[i]] = i+1
        return []    
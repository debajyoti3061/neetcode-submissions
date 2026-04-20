class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output = [0] * (2*len(nums))
        for i,num in enumerate(nums) :
            output[i] = output[i+len(nums)] = num
        return output
        
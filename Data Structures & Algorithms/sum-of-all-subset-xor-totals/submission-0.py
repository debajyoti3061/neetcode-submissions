"""
REVISION NOTES - Sum of All Subset XOR Totals:
• Backtracking approach to generate all possible subsets
• For each element: two choices - include it (XOR with current total) or exclude it
• DFS explores both paths: dfs(i+1, total ^ nums[i]) and dfs(i+1, total)
• Base case: when i == len(nums), return the current XOR total
• Sums all XOR totals from all possible subsets (2^n subsets total)
• Time: O(2^n), Space: O(n) for recursion depth
"""

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i,total):
            if i == len(nums):
                return total
            return dfs(i+1,total ^ nums[i]) + dfs(i+1,total)
        return dfs(0,0)        
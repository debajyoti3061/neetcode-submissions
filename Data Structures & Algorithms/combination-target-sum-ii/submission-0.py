"""
REVISION NOTES - Combination Target Sum Ii:
- Sort candidates to handle duplicates
- Use backtracking with start index to avoid reusing elements
- Skip duplicates at same recursion level
- Each element can only be used once
- Time: O(2^n), Space: O(n)
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def dfs(start, remain, temp_list) :
            if remain < 0:
                return
            elif remain == 0:
                result.append(list(temp_list))
            else :
                for i in range(start, len(candidates)):
                    if i > start and candidates[i-1] == candidates[i]:
                        continue
                    temp_list.append(candidates[i])
                    dfs(i+1,remain-candidates[i], temp_list)
                    temp_list.pop()
        dfs(0,target,[])
        return result

        
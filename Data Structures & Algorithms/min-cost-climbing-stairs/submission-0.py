"""
REVISION NOTES - Min Cost Climbing Stairs:
• Dynamic programming: modify cost array in-place
• For each step i, add minimum cost from previous two steps
• cost[i] represents minimum cost to reach step i
• Can start from step 0 or step 1, so return min of last two steps
• Space-optimized DP using input array modification
• Time: O(n), Space: O(1)
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1],cost[i-2])
        
        return min(cost[-2],cost[-1])
        
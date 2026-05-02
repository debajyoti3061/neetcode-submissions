"""
REVISION NOTES - Gas Station:
- Calculate net gas at each station (gas[i] - cost[i])
- If total net gas is negative, no solution exists
- Use greedy approach: start from station where we can complete circuit
- Reset starting point when running out of gas
- Time: O(n), Space: O(1)
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        res = 0
        for i in range(len(gas)):
            total += gas[i]-cost[i]
            if total < 0:
                total = 0
                res = i+1
        return res
        
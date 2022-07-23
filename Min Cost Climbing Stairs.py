class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = {}
        return min(self.minCost((n-1), cost, cache), self.minCost((n-2), cost, cache))
    
    def minCost(self, i, cost, cache):
        if i < 0:
            return 0
        if i == 0 or i == 1:
            return cost[i]
        if i in cache:
            return cache[i]
        cache[i] = cost[i] + min(self.minCost(i-1, cost, cache), self.minCost(i-2, cost, cache))
        
        return cache[i]
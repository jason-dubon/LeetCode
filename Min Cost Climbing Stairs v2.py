class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = {}
        
        cache1 = cost[0]
        cache2 = cost[1]
        
        for i in range(2, len(cost)):
            curr = cost[i] + min(cache1, cache2)
            cache1 = cache2
            cache2 = curr
            
        return min(cache1, cache2)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:       
        left = 1
        right = max(piles)
        if h == len(piles):
            return right
        
        minK = right
        while left <= right:
            k = (left + right) // 2
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i]/k)    
                if hours > h:
                    left = k + 1
                    break
            if hours <= h:
                minK = min(minK, k)
                right = k - 1
                
        return minK

                    
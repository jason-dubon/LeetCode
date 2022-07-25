class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        
        first = -1
        while left <= right:
            mid = (left + right) // 2 
            
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                first = mid
                right = mid - 1
        
        if first == -1:
            return [-1, -1]
        
        l = 0
        r = len(nums) - 1
        last = -1
        
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                last = m
                l = m + 1
                    
        return [first, last]
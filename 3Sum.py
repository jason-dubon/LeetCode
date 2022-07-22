class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                calc = num + nums[left] + nums[right]
                if calc == 0:
                    res.append([num, nums[left], nums[right]])
                    
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif calc > 0:
                    right -= 1
                elif calc < 0:
                    left += 1

        return res
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mymap = {}
        for i, num in enumerate(nums):
            mymap[num] = i
        
        for i in range(len(nums)):
            look = target - nums[i]
            if look in mymap and mymap[look] != i:
                index1 = mymap[look]
                return [index1, i]
            
        return None
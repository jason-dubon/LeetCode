class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {}

        for i in range(len(nums)):
            look = target - nums[i]
            if look in mymap and mymap[look] != i:
                index1 = mymap[look]
                return [index1, i]
            # this needs to be after the if statment in case there are duplicate values that equal target
            mymap[nums[i]] = i
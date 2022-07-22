class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left <= right:
            calc = numbers[left] + numbers[right] 
            if calc == target:
                return [left+1, right+1]
            elif calc < target:
                left += 1
            elif calc > target:
                right -= 1
            
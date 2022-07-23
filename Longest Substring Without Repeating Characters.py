class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        
       
        left = 0
        right = 0
        myset = set()
        while left < len(s) and right < len(s):
            if s[right] in myset:
                myset.remove(s[left])
                left += 1
            else:
                myset.add(s[right])
                right += 1
                maxLen = max(maxLen, len(myset))    
            
        return maxLen
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        res = 0
        mymap = {}
                
        for right in range(len(s)):
            if s[right] not in mymap:
                mymap[s[right]] = 1
            else:
                mymap[s[right]] += 1
            
            while (right - left + 1) - max(mymap.values()) > k:
                mymap[s[left]] -= 1
                left += 1
               
            res = max(res, right - left + 1)
            
        return res
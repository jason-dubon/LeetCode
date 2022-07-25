class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {"(" : ")", 
                   "{" : "}",
                   "[" : "]"}
        stack = []
        
        for i in s:
            if i in hash_map:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                curr = stack.pop()
                
                if hash_map[curr] == i:
                    continue
                else:
                    return False
        if stack:
            return False
        else:
            return True
            
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        
        stack = []
        
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")" and len(stack) == 0:
                res.append("")
                continue
            elif s[i] == ")":
                stack.pop()
            res.append(s[i])
                
        for i in stack:
            res[i] = ""
        
        return "".join(res)
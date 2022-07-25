# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfsHeight(root):
            if not root:
                return 0
            
            return 1 + dfsHeight(root.left)
        
        def nodeSearch(index, height, root):
            l = 0
            r = 2 ** (height - 1) - 1
            count = 0
            
            while count < height-1:
                midNode = math.ceil((l+r)/2)
                
                if index >= midNode:
                    root = root.right
                    l = midNode
                else:
                    root = root.left
                    r = midNode - 1
                count += 1
            
            return root != None
            
        height = dfsHeight(root)
        if height == 1:
            return 1
        
        upperBound = 2 ** (height - 1) - 1
        left, right = 0, upperBound 
        
        while left < right:
            mid = math.ceil((right+left)/2)
            if nodeSearch(mid, height, root):
                left = mid
            else:
                right = mid - 1
    
        calc = upperBound + left + 1
        return calc
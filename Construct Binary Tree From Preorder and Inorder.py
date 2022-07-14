# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        headIndex = 0
        mymap = {}
        for i in range(len(inorder)):
            mymap[inorder[i]] = i
            
            def arrayToTree(left, right):
                nonlocal headIndex
                if left > right:
                    return None
                
                rootVal = preorder[headIndex]
                root = TreeNode(rootVal)
                headIndex += 1
                
                root.left = arrayToTree(left, mymap[rootVal] - 1)
                root.right = arrayToTree(mymap[rootVal] + 1, right)
                return root
            
        return arrayToTree(0, len(preorder) - 1)
            
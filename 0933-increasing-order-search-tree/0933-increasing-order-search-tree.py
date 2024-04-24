# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        def inOrderTraversal(root):
            if root is None:
                return []
            
            return inOrderTraversal(root.left) + [root.val] + inOrderTraversal(root.right)
        
        sortedValues = inOrderTraversal(root)

        dummy = TreeNode()
        curr = dummy

        for val in sortedValues:
            curr.right = TreeNode(val)
            curr = curr.right
        
        return dummy.right
# Time Complexity : O(n) n is the number of elements which are traveresed 
# Space Complexity : O(h) here h is the the height the tree in which the elements are added in the stack 
# Did this code successfully run on Leetcode :  Yes 
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach : - Here we add the elements in the stack and keep the previous element in the a variable and if the previous is greater than the further element then we return false and stop the recursion


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = TreeNode(None)
    isValid = True
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        self.inorder(root)
        return self.isValid
 
    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        if self.prev.val !=None:
            if self.prev.val >= root.val:
                self.isValid = False
                return
        self.prev = root
        self.inorder(root.right)



## Iterative method 
#     prev = TreeNode(None)
#    # isValid = True
    
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         if root == None:
#             return True
#         stack = []
        
#         while root!=None or len(stack)!=0:
#             while root!=None:
#                 stack.append(root)
#                 root = root.left
#             root = stack.pop()
#             if self.prev.val!=None and self.prev.val >=root.val:
#                 return False
#             self.prev = root
#             root = root.right
#         return True

    
        
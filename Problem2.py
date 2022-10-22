# Time Complexity : O(n) n is the time in which the tree should be created 
# Space Complexity : O(n) here n is the size of creating the hashmap
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
    hashMap = {}
    idx = 0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder == None or len(preorder) == 0 or len(inorder)==0:
            return None 
        
        for i in range(len(inorder)):
            self.hashMap[inorder[i]] = i
        print(self.hashMap)
        
        return self.construct(preorder, inorder, 0, len(inorder)-1)

    def construct(self, preorder, inorder, start, end):

        if start > end:
            return None 
        rootVal = preorder[self.idx]
        self.idx+=1
        root = TreeNode(rootVal)
        print(rootVal)
        rootIdx = self.hashMap.get(rootVal)

        root.left = self.construct(preorder, inorder, start, rootIdx-1)
        root.right = self.construct(preorder, inorder, rootIdx+1, end)

        return root


    ### Another approach in O(n^2) time complexity and in O(n^2) space complexity
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    #     if preorder==None or len(preorder)==0 or len(inorder)==0:
    #         return None
        
    #     rootVal = preorder[0]
    #     root = TreeNode(rootVal)
    #     rootIdx = inorder.index(root.val)
    #     leftInorder = inorder[:rootIdx]
    #     rightInorder = inorder[rootIdx+1:]
    #     leftPretorder = preorder[1:len(leftInorder)+1]
    #     rightPreOrder = preorder[len(leftInorder)+1:]
    #     root.left = self.buildTree(leftPretorder, leftInorder)
    #     root.right = self.buildTree(rightPreOrder, rightInorder)

    #     return root

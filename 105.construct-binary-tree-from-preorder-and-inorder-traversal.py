# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#


# @lc tags=array;tree;depth-first-search

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
# 
# 
# 
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.helper(preorder, inorder, pre_left=0, pre_right=len(preorder) - 1, in_left=0, in_right=len(preorder) - 1)

    def helper(self, preorder, inorder, pre_left, pre_right, in_left, in_right):
        if pre_left > pre_right or in_left > in_right:
            return None
        node_val = preorder[pre_left]
        i = in_left
        while node_val != inorder[i]:
            i += 1
        return TreeNode(val=node_val, left=self.helper(preorder, inorder, pre_left=pre_left+1, pre_right=pre_left+(i - in_left), in_left=in_left, in_right=i - 1), \
                                    right=self.helper(preorder, inorder, pre_left=pre_left+(i - in_left)+1, pre_right=len(preorder) - 1, in_left=i+1, in_right=in_right))
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]')
    print('Exception :')
    print('[3,9,20,null,null,15,7]')
    print('Output :')
    print(str(Solution().buildTree([3,9,20,15,7],[9,3,15,20,7])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('preorder = [-1], inorder = [-1]')
    print('Exception :')
    print('[-1]')
    print('Output :')
    print(str(Solution().buildTree([-1],[-1])))
    print()
    
    pass
# @lc main=end
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#


# @lc tags=dynamic-programming;tree;depth-first-search

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
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.helper(preorder, 0, len(preorder) - 1)
    def helper(self, preorder, left, right):
        if left > right:
            return None
        root = TreeNode(val=preorder[left])
        if left == right:
            return root
        offset = 1
        while left + offset <= right and preorder[left] > preorder[left + offset]:
            offset += 1
        root.left = self.helper(preorder, left + 1, left + offset - 1)
        root.right = self.helper(preorder, left + offset, right)
        return root
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('preorder = [8,5,1,7,10,12]')
    print('Exception :')
    print('[8,5,10,1,7,null,12]')
    print('Output :')
    print(str(Solution().bstFromPreorder([8,5,1,7,10,12])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('preorder = [4,2]')
    print('Exception :')
    print('[4,2]')
    print('Output :')
    print(str(Solution().bstFromPreorder([4,2])))
    print()
    
    pass
# @lc main=end
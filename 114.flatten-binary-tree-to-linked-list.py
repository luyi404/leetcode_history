# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#


# @lc tags=tree;depth-first-search

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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        stk = [root]
        while stk:
            node = stk.pop()
            if node.left:
                p = node.left
                while p.right:
                    p = p.right
                p.right = node.right
                node.right = node.left
                node.left = None
            if node.right:
                stk.append(node.right)
        
        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,5,3,4,null,6]')
    print('Exception :')
    print('[1,null,2,null,3,null,4,null,5,null,6]')
    print('Output :')
    print(str(Solution().flatten(listToTreeNode([1,2,5,3,4,None,6]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().flatten(listToTreeNode([]))))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('root = [0]')
    print('Exception :')
    print('[0]')
    print('Output :')
    print(str(Solution().flatten(listToTreeNode([0]))))
    print()
    
    pass
# @lc main=end
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#


# @lc tags=binary-search;tree

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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = 1
        t = root.left
        while t:
            left += 1
            t = t.left
        t = root.right
        right = 1
        while t:
            right += 1
            t = t.right
        if left == right:
            return pow(2, left) - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1

# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,3,4,5,6]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().countNodes(listToTreeNode([1,2,3,4,5,6]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().countNodes(listToTreeNode([]))))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('root = [1]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().countNodes(listToTreeNode([1]))))
    print()
    
    pass
# @lc main=end
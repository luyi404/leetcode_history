# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#


# @lc tags=tree;depth-first-search;breadth-first-search

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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = [root]
        depth = 0
        while q:
            depth += 1
            for _ in range(len(q)):
                node = q.pop(0)
                if not node.left and not node.right:
                    return depth
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,9,20,null,null,15,7]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().minDepth(listToTreeNode([3,9,20,None,None,15,7]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [2,null,3,null,4,null,5,null,6]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().minDepth(listToTreeNode([2,None,3,None,4,None,5,None,6]))))
    print()
    
    pass
# @lc main=end
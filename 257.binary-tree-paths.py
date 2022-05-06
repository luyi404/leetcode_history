# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = self.helper(root)
        ans = []
        for path in paths:
            ans.append('->'.join(path))
        return ans
    def helper(self, root: TreeNode):
        if not root.left and not root.right:
            return [[str(root.val)]]
        ans = list()
        if root.left:
            left = self.helper(root.left)
            for l in left:
                l.insert(0, str(root.val))
            ans += left
        if root.right:
            right = self.helper(root.right)
            for r in right:
                r.insert(0, str(root.val))
            ans += right
        return ans
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,3,null,5]')
    print('Exception :')
    print('["1->2->5","1->3"]')
    print('Output :')
    print(str(Solution().binaryTreePaths(listToTreeNode([1,2,3,None,5]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [1]')
    print('Exception :')
    print('["1"]')
    print('Output :')
    print(str(Solution().binaryTreePaths(listToTreeNode([1]))))
    print()
    
    pass
# @lc main=end
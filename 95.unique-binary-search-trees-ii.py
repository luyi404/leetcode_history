# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#


# @lc tags=dynamic-programming;tree

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
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        return self.helper(1, n)

    def helper(self, left: int, right: int):
        if left > right:
            return [None]
        ans = []
        for i in range(left, right + 1):
            left_res = self.helper(left, i - 1)
            right_res = self.helper(i + 1, right)
            for l in left_res:
                for r in right_res:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    ans.append(node)
        return ans
        


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 3')
    print('Exception :')
    print('[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]')
    print('Output :')
    print(str(Solution().generateTrees(3)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('[[1]]')
    print('Output :')
    print(str(Solution().generateTrees(1)))
    print()
    
    pass
# @lc main=end
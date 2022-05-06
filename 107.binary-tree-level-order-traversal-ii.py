# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#


# @lc tags=tree;breadth-first-search

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
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        stk = [root]
        while stk:
            sub_ans = []
            for _ in range(len(stk)):
                node = stk.pop(0)
                sub_ans.append(node.val)
                if node.left:
                    stk.append(node.left)
                if node.right:
                    stk.append(node.right)
            ans.insert(0, sub_ans)
        return ans
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,9,20,null,null,15,7]')
    print('Exception :')
    print('[[15,7],[9,20],[3]]')
    print('Output :')
    print(str(Solution().levelOrderBottom(listToTreeNode([3,9,20,None,None,15,7]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [1]')
    print('Exception :')
    print('[[1]]')
    print('Output :')
    print(str(Solution().levelOrderBottom(listToTreeNode([1]))))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().levelOrderBottom(listToTreeNode([]))))
    print()
    
    pass
# @lc main=end
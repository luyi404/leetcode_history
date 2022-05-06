# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#


# @lc tags=stack;tree

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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.result = []
        self.helper(root)
        return self.result

    def helper(self, node: TreeNode):
        if node.left:
            self.helper(node.left)
        if node.right:
            self.helper(node.right)
        self.result.append(node.val)
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,null,2,3]')
    print('Exception :')
    print('[3,2,1]')
    print('Output :')
    print(str(Solution().postorderTraversal(listToTreeNode([1,None,2,3]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().postorderTraversal(listToTreeNode([]))))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('root = [1]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().postorderTraversal(listToTreeNode([1]))))
    print()
    
    pass
# @lc main=end
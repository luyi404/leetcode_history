# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#


# @lc tags=hash-table;stack;tree

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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
    #     self.result = []
    #     self.helper(root)
    #     return self.result

    # def helper(self, node: TreeNode):
    #     if node.left:
    #         self.helper(node.left)
    #     self.result.append(node.val)
    #     if node.right:
    #         self.helper(node.right)
        result = []
        p = root
        stk = []
        while len(stk) != 0 or p:
            while p:
                stk.append(p)
                p = p.left
            p = stk.pop()
            result.append(p.val)
            p = p.right
        return result
            
        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,null,2,3]')
    print('Exception :')
    print('[1,3,2]')
    print('Output :')
    print(str(Solution().inorderTraversal(listToTreeNode([1,None,2,3]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().inorderTraversal(listToTreeNode([]))))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('root = [1]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().inorderTraversal(listToTreeNode([1]))))
    print()
    
    pass
# @lc main=end
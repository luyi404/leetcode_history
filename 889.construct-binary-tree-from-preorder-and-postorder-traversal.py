# @lc app=leetcode id=889 lang=python3
#
# [889] Construct Binary Tree from Preorder and Postorder Traversal
#


# @lc tags=string

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
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        return self.helper(preorder=preorder, postorder=postorder, pre_l=0, pre_r=n - 1, post_l=0, post_r=n - 1)
    def helper(self, preorder, postorder, pre_l, pre_r, post_l, post_r):
        if pre_l > pre_r or post_l > post_r:
            return None
        root = TreeNode(val=preorder[pre_l])
        if pre_l == pre_r:
            return root
        else:
            left_val = preorder[pre_l + 1]
            offset = 0
            while postorder[post_l + offset] != left_val:
                offset += 1
            # value of offset = length of left sub-tree
            root.left = self.helper(preorder, postorder, pre_l + 1, pre_l + 1 + offset, post_l, post_l + offset)
            root.right = self.helper(preorder, postorder, pre_l + 1 + offset + 1, pre_r, post_l + offset + 1, post_r - 1)
            return root

# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]')
    print('Exception :')
    print('[1,2,3,4,5,6,7]')
    print('Output :')
    print(str(Solution().constructFromPrePost([1,2,4,5,3,6,7],[4,5,2,6,7,3,1])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('preorder = [1], postorder = [1]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().constructFromPrePost([1],[1])))
    print()
    
    pass
# @lc main=end
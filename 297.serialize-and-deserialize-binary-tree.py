# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#


# @lc tags=tree;design

# @lc imports=start
import re
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
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        ans = ''
        self.serial_helper(root, ans)
        return ans.strip('_')
    
    def serial_helper(self, root, ans):
        if not root:
            ans += '_n'
            return
        ans += '_{}'.format(str(root.val))
        self.serial_helper(root.left, ans)
        self.serial_helper(root.right, ans)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        ans = data.split('_')
        print(data)
        return self.de_helper(ans, 0)

    def de_helper(self, ans, i):
        if i >= len(ans):
            return
        if ans[i] != 'n':
            t = root = TreeNode(eval(ans[i]))
            ii = i + 1
            while ans[ii] != 'n':
                t.left = self.de_helper(ans, ii)
                ii += 1
                t = t.left
            root.right = self.de_helper(ans, ii + 1)
            return root
        else:
            return None

    
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(Codec.serialize(listToTreeNode([1,2,3,None,None,4,5])))
    pass
# @lc main=end
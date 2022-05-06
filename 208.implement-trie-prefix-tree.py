# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#


# @lc tags=design;trie

# @lc imports=start
# from imports import *
# @lc imports=end

# @lc idea=start
# 
# 
# 
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
from re import T


class TreeNode:
    def __init__(self,val, childrens: list['TreeNode'] = []):
        self.val = val
        self.childrens = childrens

class Trie:

    def __init__(self):
        self.root = TreeNode("")
        

    def insert(self, word: str) -> None:
        n = len(word)
        cur = self.root
        i = 0
        while i < n:
            t = 0
            flag = False
            while t < len(cur.childrens):
                if cur.childrens[t].val == word[i]:
                    cur = cur.childrens[t]
                    i += 1
                    flag = True
                    break
                else:
                    t += 1
            if flag:
                continue
            if t == len(cur.childrens):
                print(cur.val)
                cur.childrens.append(TreeNode(val=word[i]))
                cur = cur.childrens[-1]
                i += 1
        

    def search(self, word: str) -> bool:
        cur = self.root
        n = len(word)
        i = 0
        while i < n:
            t = 0
            flag = False
            while t < len(cur.childrens):
                if cur.childrens[t].val == word[i]:
                    cur = cur.childrens[t]
                    i += 1
                    flag = True
                    break
                else:
                    t += 1
            if flag:
                continue
            if t == len(cur.childrens):
                return False
        return True if len(cur.childrens) == 0 else False

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    obj = Trie()
    for word in [["apple"]]:
        obj.insert(word[0])
    cur = obj.root
    print(obj.search('apple'))
    pass
# @lc main=end
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#


# @lc tags=stack;greedy

# @lc imports=start
from re import T
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
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "bcabc"')
    print('Exception :')
    print('"abc"')
    print('Output :')
    print(str(Solution().removeDuplicateLetters("bcabc")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "cbacdcbc"')
    print('Exception :')
    print('"acdb"')
    print('Output :')
    print(str(Solution().removeDuplicateLetters("cbacdcbc")))
    print()
    
    pass
# @lc main=end
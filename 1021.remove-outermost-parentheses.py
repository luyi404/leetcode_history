# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
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
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ''
        level = 0
        for i in s:
            if i == ')':
                level -= 1
            if level >= 1:
                ans += i
            if i == '(':
                level += 1
        return ans
        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "(()())(())"')
    print('Exception :')
    print('"()()()"')
    print('Output :')
    print(str(Solution().removeOuterParentheses("(()())(())")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "(()())(())(()(()))"')
    print('Exception :')
    print('"()()()()(())"')
    print('Output :')
    print(str(Solution().removeOuterParentheses("(()())(())(()(()))")))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('s = "()()"')
    print('Exception :')
    print('""')
    print('Output :')
    print(str(Solution().removeOuterParentheses("()()")))
    print()
    
    pass
# @lc main=end
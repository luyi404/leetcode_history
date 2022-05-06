# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#


# @lc tags=Unknown

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
    def backspaceCompare(self, s: str, t: str) -> bool:
        stk1 = []
        stk2 = []
        for i in s:
            if i == '#':
                if stk1:
                    stk1.pop()
            else:
                stk1.append(i)
        for i in t:
            if i == '#':
                if stk2:
                    stk2.pop()
            else:
                stk2.append(i)
        if len(stk1) == len(stk2):
            for i in range(len(stk1)):
                if stk1[i] != stk2[i]:
                    return False
            return True
        else:
            return False

# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().backspaceCompare("y#fo##f","y#f#o##f")))
    print()
    
    # print('Example 2:')
    # print('Input : ')
    # print('s = "ab##", t = "c#d#"')
    # print('Exception :')
    # print('true')
    # print('Output :')
    # print(str(Solution().backspaceCompare("ab##","c#d#")))
    # print()
    
    # print('Example 3:')
    # print('Input : ')
    # print('s = "a#c", t = "b"')
    # print('Exception :')
    # print('false')
    # print('Output :')
    # print(str(Solution().backspaceCompare("a#c","b")))
    # print()
    
    pass
# @lc main=end
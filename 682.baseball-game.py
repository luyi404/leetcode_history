# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#


# @lc tags=stack

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
    def calPoints(self, ops: List[str]) -> int:
        stk = []
        for op in ops:
            if op == "+":
                t1 = stk.pop()
                t2 = stk.pop()
                stk.append(t2)
                stk.append(t1)
                stk.append(t1 + t2)
            elif op == "D":
                stk.append(stk[-1] * 2)
            elif op == "C":
                stk.pop()
            else:
                stk.append(eval(op))
        return sum(stk)
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    # print('Example 1:')
    # print('Input : ')
    # print('ops = ["5","2","C","D","+"]')
    # print('Exception :')
    # print('30')
    # print('Output :')
    # print(str(Solution().calPoints(["5","2","C","D","+"])))
    # print()
    
    print('Example 2:')
    print('Input : ')
    print('ops = ["5","-2","4","C","D","9","+","+"]')
    print('Exception :')
    print('27')
    print('Output :')
    print(str(Solution().calPoints(["5","-2","4","C","D","9","+","+"])))
    print()
    
    # print('Example 3:')
    # print('Input : ')
    # print('ops = ["1"]')
    # print('Exception :')
    # print('1')
    # print('Output :')
    # print(str(Solution().calPoints(["1"])))
    # print()
    
    pass
# @lc main=end
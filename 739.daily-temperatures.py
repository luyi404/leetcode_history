# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#


# @lc tags=hash-table;stack

# @lc imports=start
from ast import Num
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
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        ans = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stk and t > temperatures[stk[-1]]:
                ind = stk.pop()
                ans[ind] = i - ind
            stk.append(i)

        return ans
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('temperatures = [73,74,75,71,69,72,76,73]')
    print('Exception :')
    print('[1,1,4,2,1,1,0,0]')
    print('Output :')
    print(str(Solution().dailyTemperatures([73,74,75,71,69,72,76,73])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('temperatures = [30,40,50,60]')
    print('Exception :')
    print('[1,1,1,0]')
    print('Output :')
    print(str(Solution().dailyTemperatures([30,40,50,60])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('temperatures = [30,60,90]')
    print('Exception :')
    print('[1,1,0]')
    print('Output :')
    print(str(Solution().dailyTemperatures([30,60,90])))
    print()
    
    pass
# @lc main=end
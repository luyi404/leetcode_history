# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#


# @lc tags=stack;greedy

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
    def removeKdigits(self, num: str, k: int) -> str:
        ans = list(num)
        stk = []
        counter = 0
        for i in range(len(num)):
            if counter == k:
                break
            while stk and int(num[i]) < int(num[stk[-1]]):
                if counter == k:
                    break
                ans[stk.pop()] = ''
                counter += 1
            stk.append(i)
        ans = ''.join(ans)
        while counter < k:
            ans = ans[:-1]
            counter += 1
        if not ans:
            return "0"
        return str(int(ans))
        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('num = "1432219", k = 3')
    print('Exception :')
    print('"1219"')
    print('Output :')
    print(str(Solution().removeKdigits("1432219",3)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('num = "10200", k = 1')
    print('Exception :')
    print('"200"')
    print('Output :')
    print(str(Solution().removeKdigits("10200",1)))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('num = "10", k = 2')
    print('Exception :')
    print('"0"')
    print('Output :')
    print(str(Solution().removeKdigits("10",2)))
    print()
    
    pass
# @lc main=end
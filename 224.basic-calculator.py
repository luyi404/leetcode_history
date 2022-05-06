# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#


# @lc tags=math;stack

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
priorityLevel = {
    '+': 0,
    '-': 0,
    '(': 1,
    ')': 1
}


class Solution:
    def calculate(self, s):
        stack = []
        result = 0
        number = 0
        sign = 1
        for c in s:
            if c == '':
                continue
            if c in '1234567890':
                number = number * 10 + int(c)
            elif c == '+':
                result += (sign * number)
                number = 0
                sign = 1
            elif c == '-':
                result += (sign * number)
                number = 0
                sign = -1
            elif c == '(':
                stack.append(sign)
                stack.append(result)
                sign = 1
                result = 0
                number = 0
            elif c == ')':
                result += (sign * number)
                result = stack.pop() + stack.pop() * result
                sign = 1
                number = 0
        if number != 0:
            result += (sign * number)
        return result

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "1 + 1"')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().calculate("1 + 1")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = " 2-1 + 2 "')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().calculate(" 2-1 + 2 ")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "(1+(4+5+2)-3)+(6+8)"')
    print('Exception :')
    print('23')
    print('Output :')
    print(str(Solution().calculate("(1+(4+5+2)-3)+(6+8)")))
    print()

    pass
# @lc main=end

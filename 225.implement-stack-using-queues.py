# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#


# @lc tags=stack;design

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
class MyStack:

    def __init__(self):
        self.q_push = []
        self.q_pop = []

    def push(self, x: int) -> None:
        self.q_push.append(x)

    def pop(self) -> int:
        t = None
        while self.q_push:
            t = self.q_push.pop(0)
            if self.q_push:
                self.q_pop.append(t)
        self.q_push = self.q_pop
        self.q_pop = []
        return t

    def top(self) -> int:
        t = None
        while self.q_push:
            t = self.q_push.pop(0)
            self.q_pop.append(t)
        self.q_push = self.q_pop
        self.q_pop = []
        return t

        
    def empty(self) -> bool:
        return not self.q_push and not self.q_pop
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    print(str(Solution().__init__()))
    print()
    
    pass
# @lc main=end
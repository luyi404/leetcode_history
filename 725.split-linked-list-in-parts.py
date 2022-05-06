# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#


# @lc tags=linked-list

# @lc imports=start
from multiprocessing import dummy
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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        result = [None] * k
        if not head or k == 0:
            return result
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        quotient, reminder = count // k, count % k
        curr = dummy_head = ListNode(-1, head)
        for i in range(k):
            result[i] = curr
            for _ in range(quotient):
                curr = curr.next
            if reminder > 0:
                curr = curr.next
                reminder -= 1
            next = curr.next
            curr.next = None
            curr = ListNode(-1, next)
        for i in range(k):
            result[i] = result[i].next
        return result
            
            
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3], k = 5')
    print('Exception :')
    print('[[1],[2],[3],[],[]]')
    print('Output :')
    print(str(Solution().splitListToParts(listToListNode([1,2,3]),5)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('head = [1,2,3,4,5,6,7,8,9,10], k = 3')
    print('Exception :')
    print('[[1,2,3,4],[5,6,7],[8,9,10]]')
    print('Output :')
    print(str(Solution().splitListToParts(listToListNode([1,2,3,4,5,6,7,8,9,10]),3)))
    print()
    
    pass
# @lc main=end
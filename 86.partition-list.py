# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#


# @lc tags=linked-list;two-pointers

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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy_head = ListNode(-1, head)
        fast = dummy_head
        while fast.next and fast.next.val < x:
            fast = fast.next
        next_head = fast.next
        curr = next_head
        while curr and curr.next:
            if curr.next.val < x:
                next = curr.next
                curr.next = curr.next.next
                fast.next = next
                fast.next.next = next_head
                fast = fast.next
            else:
                curr = curr.next

        return dummy_head.next
        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,4,3,0,2,5,2], x = 3')
    print('Exception :')
    print('[1,0,2,2,4,3,5]')
    print('Output :')
    print(str(Solution().partition(listToListNode([1,4,3,0,2,5,2]),3)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('head = [2,1], x = 2')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().partition(listToListNode([2,1]),2)))
    print()
    
    pass
# @lc main=end
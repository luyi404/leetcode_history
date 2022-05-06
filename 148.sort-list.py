# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#


# @lc tags=linked-list;sort

# @lc imports=start
from locale import currency
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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        last_head = slow.next
        slow.next = None
        return self.merge(self.sortList(head), self.sortList(last_head))
    def merge(self, l1, l2):
        dummy_head = ListNode()
        curr = dummy_head
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return dummy_head.next


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [4,2,1,3]')
    print('Exception :')
    print('[1,2,3,4]')
    print('Output :')
    print(str(Solution().sortList(listToListNode([4,2,1,3]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('head = [-1,5,3,4,0]')
    print('Exception :')
    print('[-1,0,3,4,5]')
    print('Output :')
    print(str(Solution().sortList(listToListNode([-1,5,3,4,0]))))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('head = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().sortList(listToListNode([]))))
    print()
    
    pass
# @lc main=end
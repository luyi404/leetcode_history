# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#


# @lc tags=linked-list;sort

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
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy_head = ListNode(-1, head)
        fast = dummy_head
        # 对fast.next去比较
        while fast and fast.next:
            curr = dummy_head
            while curr.next and curr.next != fast.next and curr.next.val < fast.next.val:
                curr = curr.next
            if curr != fast:
                next = curr.next
                curr.next = fast.next
                fast.next = fast.next.next
                curr.next.next = next
            else:
                fast = fast.next
        return dummy_head.next
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [4,2,1,3]')
    print('Exception :')
    print('[1,2,3,4]')
    print('Output :')
    print(str(Solution().insertionSortList(listToListNode([4,2,1,3]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('head = [-1,5,3,4,0]')
    print('Exception :')
    print('[-1,0,3,4,5]')
    print('Output :')
    print(str(Solution().insertionSortList(listToListNode([-1,5,3,4,0]))))
    print()
    
    pass
# @lc main=end
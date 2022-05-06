# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy_head = ListNode(-1)
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 if list1 else list2
        return dummy_head.next

# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('list1 = [1,2,4], list2 = [1,3,4]')
    print('Exception :')
    print('[1,1,2,3,4,4]')
    print('Output :')
    print(str(Solution().mergeTwoLists(listToListNode([1,2,4]),listToListNode([1,3,4]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('list1 = [], list2 = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().mergeTwoLists(listToListNode([]),listToListNode([]))))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('list1 = [], list2 = [0]')
    print('Exception :')
    print('[0]')
    print('Output :')
    print(str(Solution().mergeTwoLists(listToListNode([]),listToListNode([0]))))
    print()
    
    pass
# @lc main=end
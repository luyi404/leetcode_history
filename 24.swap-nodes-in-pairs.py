# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#


# @lc tags=linked-list

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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy_head = ListNode(-1, head)
        curr = dummy_head
        while curr and curr.next and curr.next.next:
            next = curr.next.next.next
            curr.next.next.next = curr.next
            curr.next = curr.next.next
            curr.next.next.next = next
            curr = curr.next.next
        return dummy_head.next
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4]')
    print('Exception :')
    print('[2,1,4,3]')
    print('Output :')
    print(str(Solution().swapPairs(listToListNode([1,2,3,4]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('head = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().swapPairs(listToListNode([]))))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('head = [1]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().swapPairs(listToListNode([1]))))
    print()
    
    pass
# @lc main=end
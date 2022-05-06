# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        even_head = head.next
        curr = head
        flag = True
        pre = None
        while curr and curr.next:
            next = curr.next
            curr.next = curr.next.next
            pre, curr = curr, next
            flag = not flag
        if flag:
            curr.next = even_head
        else:
            pre.next = even_head
        return head

# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4,5]')
    print('Exception :')
    print('[1,3,5,2,4]')
    print('Output :')
    print(str(Solution().oddEvenList(listToListNode([1,2,3,4,5]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('head = [2,1,3,5,6,4,7]')
    print('Exception :')
    print('[2,3,6,7,1,5,4]')
    print('Output :')
    print(str(Solution().oddEvenList(listToListNode([2,1,3,5,6,4,7]))))
    print()
    
    pass
# @lc main=end
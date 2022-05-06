# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#


# @lc tags=Unknown

# @lc imports=start
from email import header
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
class MyLinkedList:
    class Node():
        def __init__(self, x = 0, next = None) -> None:
            self.val = x
            self.next = next

    def __init__(self):
        self.head = None
        self.num = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.num:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val
         

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = MyLinkedList.Node(x = val, next = None)
        else:
            newNode = MyLinkedList.Node(x = val, next = self.head)
            self.head = newNode
        self.num += 1

    def addAtTail(self, val: int) -> None:
        if self.num == 0:
            self.head = MyLinkedList.Node(x = val, next = None)
            self.num += 1
            return 
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = MyLinkedList.Node(x = val, next = None)
        self.num += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.num:
            return 
        if index == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            next = curr.next
            curr.next = MyLinkedList.Node(val, next)
            self.num += 1
            
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.num:
            return
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
        self.num -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

# @lc main=start
if __name__ == '__main__':

    
    pass
# @lc main=end
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#


# @lc tags=divide-and-conquer;heap

# @lc imports=start
from turtle import position
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
def swap(nums: list, i1, i2):
    t = nums[i1]
    nums[i1] = nums[i2]
    nums[i2] = t

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        while True:
            position = self.partition(nums, l, r)
            if position == k - 1:
                return nums[position]
            if position > k - 1:
                r = position - 1
            else:
                l = position + 1


    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot = nums[left]
        l, r = left + 1, right
        while l <= r:
            if nums[l] < pivot and nums[r] > pivot:
                swap(nums, l, r)
                l, r = l+1, r-1
            if nums[l] >= pivot:
                l += 1
            if nums[r] <= pivot:
                r -= 1
        swap(nums, left, r)
        return r

        

# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [3,2,1,5,6,4], k = 2')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().findKthLargest([3,2,1,5,6,4],2)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [3,2,3,1,2,4,5,5,6], k = 4')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().findKthLargest([3,2,3,1,2,4,5,5,6],4)))
    print()
    
    pass
# @lc main=end
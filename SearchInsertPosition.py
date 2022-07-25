"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
"""
"""
給定一個由不同整數組成的排序數組和一個目標值，如果找到目標，則返回索引。如果不是，則返回按順序插入的索引。
您必須編寫一個具有 O(log n) 運行時復雜度的算法。
"""
"""
case1:
    Runtime: 27 ms, faster than 98.67% of Python online submissions for Search Insert Position.
    Memory Usage: 14.3 MB, less than 7.72% of Python online submissions for Search Insert Position.
case2:
    Runtime: 33 ms, faster than 91.81% of Python online submissions for Search Insert Position.
    Memory Usage: 14.1 MB, less than 78.21% of Python online submissions for Search Insert Position.
"""



class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)


class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        for i in range(len(nums)):
            if i + 1 < len(nums):
                if nums[i] < target < nums[i + 1]:
                    return i + 1
            elif target > nums[-1]:
                return len(nums)
            else:
                return 0


sol = Solution().searchInsert([1], 0)
print(sol)

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""
"""
給定一個整數數組 nums 和一個整數目標，返回兩個數字的索引，使它們加起來等於目標。
您可能會假設每個輸入都只有一個解決方案，並且您可能不會兩次使用相同的元素。
您可以按任何順序返回答案。
"""
"""
Runtime: 62 ms, faster than 77.76% of Python online submissions for Two Sum.
Memory Usage: 14.5 MB, less than 22.19% of Python online submissions for Two Sum.
"""


class Solution:
    def twoSum(self, nums, target):
        nums_map = {}
        for i in range(len(nums)):
            if nums_map.__contains__(target - nums[i]):
                return [i, nums_map.get(target - nums[i])]
            else:
                nums_map[nums[i]] = i


sol = Solution().twoSum([3, 2, 3, 4], 6)
print(sol)

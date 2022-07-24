"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.
Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates,
then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""
"""
給定一個整數數組 nums 和一個整數 val，就地刪除 nums 中所有出現的 val。元素的相對順序可能會改變。
由於在某些語言中無法更改數組的長度，因此您必須將結果放在數組 nums 的第一部分。
更正式地說，如果刪除重複項後有 k 個元素，則 nums 的前 k 個元素應該保存最終結果。在前 k 個元素之外留下什麼並不重要。
將最終結果放入 nums 的前 k 個槽後返回 k。
不要為另一個數組分配額外的空間。您必須通過使用 O(1) 額外內存就地修改輸入數組來做到這一點。
"""
"""
Runtime: 36 ms, faster than 29.91% of Python online submissions for Remove Element.
Memory Usage: 13.2 MB, less than 86.80% of Python online submissions for Remove Element.
"""


class Solution:
    def removeElement(self, nums, val):
        index = 0
        len_nums = len(nums)
        while index <= len_nums - 1:
            if nums[index] == val:
                del nums[index]
                len_nums -= 1
            else:
                index += 1
        return len_nums


sol = Solution().removeElement(
    [0, 1, 2, 2, 3, 0, 4, 2], 2)
print(sol)

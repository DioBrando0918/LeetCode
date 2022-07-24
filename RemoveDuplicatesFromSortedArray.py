"""
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums. More formally,
if there are k elements after removing the duplicates,
then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
Custom Judge:
The judge will test your solution with the following code:
"""
"""
給定一個按非降序nums排序的整數數組，就地刪除重複項，使每個唯一元素只出現一次。元素的相對順序應該保持不變。
由於在某些語言中無法更改數組的長度，因此您必須將結果放在數組的第一部分nums。k更正式地說，如果刪除重複項後還有元素，
那麼 的第一個k元素nums 應該保存最終結果。k 除了第一個元素之外，你留下什麼並不重要 。
k將最終結果放入 的第一個k插槽後返回nums。
不要為另一個數組分配額外的空間。您必須通過使用 O(1) 額外內存就地修改輸入數組來做到這一點。
"""

"""
Runtime: 202 ms, faster than 13.98% of Python online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 14.6 MB, less than 78.06% of Python online submissions for Remove Duplicates from Sorted Array.
Next challenges:
"""


class Solution:
    def removeDuplicates(self, nums):
        len_nums = len(nums)
        index = 0
        while index < len_nums - 1:
            if nums[index] == nums[index + 1]:
                del nums[index]
                len_nums -= 1
            else:
                index += 1
        return len(nums)


sol = Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
print(sol)

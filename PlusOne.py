"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
"""
"""
給定一個表示為整數數組digits 的大整數，其中每個digits[i] 是整數的第i 個數字。數字按從左到右的順序從最高有效到最低有效排序。大整數不包含任何前導 0。
將大整數加一併返回結果數字數組。
"""
"""
Runtime: 30 ms, faster than 47.23% of Python online submissions for Plus One.
Memory Usage: 13.4 MB, less than 68.49% of Python online submissions for Plus One.
"""


class Solution:
    def plusOne(self, digits):
        string = str()
        for i in digits:
            string += str(i)
        string = str(int(string) + 1)
        return [int(j) for j in string]


sol = Solution().plusOne([9, 9])
print(sol)

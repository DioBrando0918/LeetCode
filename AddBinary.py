"""
Given two binary strings a and b, return their sum as a binary string.
"""
"""
Runtime: 36 ms, faster than 42.92% of Python online submissions for Add Binary.
Memory Usage: 13.6 MB, less than 48.24% of Python online submissions for Add Binary.
"""


class Solution:
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]  # int() 默認輸入10進制


sol = Solution().addBinary("11", "0")
print(sol)

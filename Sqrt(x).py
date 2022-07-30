"""
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
"""
"""
給定一個非負整數 x，計算並返回 x 的平方根。
由於返回類型是整數，所以十進制數字被截斷，只返回結果的整數部分。
注意：您不能使用任何內置的指數函數或運算符，例如 pow(x, 0.5) 或 x ** 0.5。
"""
"""
Runtime: 4361 ms, faster than 5.03% of Python online submissions for Sqrt(x).
Memory Usage: 13.3 MB, less than 83.08% of Python online submissions for Sqrt(x).
"""

class Solution:
    def mySqrt(self, x):
        if x <= 1:
            return x
        num = 2
        while True:
            if num ** 2 > x:
                return num - 1
            num += 1


sol = Solution().mySqrt(100)
print(sol)

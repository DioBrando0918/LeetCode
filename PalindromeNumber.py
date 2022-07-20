"""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.
"""
"""
給定一個整數 x，如果 x 是回文整數，則返回 true。
當一個整數向後讀和向前讀一樣時，它就是一個回文數。
例如，121 是回文，而 123 不是。
"""
"""
Runtime: 57 ms, faster than 91.16% of Python online submissions for Palindrome Number.
Memory Usage: 13.2 MB, less than 85.03% of Python online submissions for Palindrome Number.
"""


class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        elif str(x) == str(abs(x))[::-1]:
            return True
        else:
            return False


sol = Solution().isPalindrome(-121)
print(sol)

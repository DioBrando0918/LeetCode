"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

"""
Runtime: 20 ms, faster than 83.79% of Python online submissions for Valid Parentheses.
Memory Usage: 13.7 MB, less than 32.35% of Python online submissions for Valid Parentheses.
"""

class Solution:
    def isValid(self, s):
        left = "([{"
        dic = {")": "(", "]": "[", "}": "{"}
        stack = []
        for i in s:
            if i in left:
                stack.append(i)
            else:
                if not stack or dic[i] != stack.pop():
                    return False
        if not stack:
            return True


sol = Solution().isValid("()[]{}")
print(sol)

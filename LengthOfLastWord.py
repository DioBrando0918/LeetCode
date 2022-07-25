"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
"""
"""
給定一個由單詞和空格組成的字符串 s，返回字符串中最後一個單詞的長度。
單詞是僅由非空格字符組成的最大子串。
"""
"""
Runtime: 11 ms, faster than 98.23% of Python online submissions for Length of Last Word.
Memory Usage: 13.4 MB, less than 91.93% of Python online submissions for Length of Last Word.
"""


class Solution:
    def lengthOfLastWord(self, s):
        lst = s.split()
        return len(lst[-1])


sol = Solution().lengthOfLastWord("luffy is still joyboy")
print(sol)

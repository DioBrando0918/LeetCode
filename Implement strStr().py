"""
Implement strStr().
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""
"""
實現 strStr()。
給定兩個字符串 needle 和 haystack，返回 haystack 中第一次出現 needle 的索引，如果 needle 不是 haystack 的一部分，則返回 -1。
澄清：
當 needle 為空字符串時，我們應該返回什麼？這是面試時問的好問題。
為了解決這個問題，當 needle 為空字符串時，我們將返回 0。這與 C 的 strstr() 和 Java 的 indexOf() 一致。
"""
"""
Runtime: 27 ms, faster than 45.68% of Python online submissions for Implement strStr().
Memory Usage: 13.2 MB, less than 95.42% of Python online submissions for Implement strStr().
"""


class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        index = 0
        while index <= len(haystack) - len(needle):
            if haystack[index:index + len(needle)] == needle:
                return index
            else:
                index += 1
        return -1


sol = Solution().strStr("aaaaa", "bba")
print(sol)

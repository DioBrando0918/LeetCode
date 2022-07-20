"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""
"""
編寫一個函數來查找字符串數組中最長的公共前綴字符串。
如果沒有公共前綴，則返回一個空字符串“”。
"""
"""
Runtime: 23 ms, faster than 83.97% of Python online submissions for Longest Common Prefix.
Memory Usage: 13.8 MB, less than 32.90% of Python online submissions for Longest Common Prefix.
"""


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        min_len = min(map(len, strs))
        count = 0
        while count < len(strs) - 1:  # if len = 3 需比較2次
            for i in range(min_len):
                if strs[count][:min_len] == strs[count + 1][:min_len]:
                    continue
                else:
                    min_len -= 1
            count += 1
        return strs[0][:min_len]


sol = Solution().longestCommonPrefix(["flower", "flow", "flight"])
print(sol)

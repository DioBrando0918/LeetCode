"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
"""
你正在爬樓梯。到達頂峰需要 n 步。
每次您可以爬 1 或 2 級台階。你可以通過多少種不同的方式爬上頂峰？
"""
"""
Runtime: 18 ms, faster than 83.60% of Python online submissions for Climbing Stairs.
Memory Usage: 13.1 MB, less than 96.83% of Python online submissions for Climbing Stairs.
"""
class Solution:
    def climbStairs(self, n):
        path = {1: 1, 2: 2, 3: 3}
        step = 0
        if n in path.keys():
            return path[n]
        for i in range(4, n + 1):
            step = path[i - 1] + path[i - 2]
            path[i] = step
        return path[n]


sol = Solution().climbStairs(8)
print(sol)

"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
"""
"""
給定排序鍊錶的頭部，刪除所有重複項，使每個元素只出現一次。返回排序好的鍊錶。
"""
"""
Runtime: 40 ms, faster than 59.09% of Python online submissions for Remove Duplicates from Sorted List.
Memory Usage: 13.4 MB, less than 66.02% of Python online submissions for Remove Duplicates from Sorted
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        current = head
        while current:
            runner = current.next
            while runner and current.val == runner.val:
                runner = runner.next
            current.next = runner
            current = runner
        return head


head = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(2)
n3 = ListNode(3)

head.next = n1
n1.next = n2
n2.next = n3

sol = Solution().deleteDuplicates(head)
while sol:
    print(sol.val)
    sol = sol.next

# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/

# Date: Dec 23, 2023
# Difficulty: Medium

from linkedlist import *

# Solution
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if head is None or left == right:
            return head

        root = start = ListNode(None)
        root.next = head

        # go to the starting and ending points
        for _ in range(left - 1):
            start = start.next
        end = start.next

        # iteratively change the nodes
        for _ in range(right - left):
            temp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = temp

        return root.next

# Test case
solution = Solution()
head = [1,2,3,4,5]
left = 2; right = 4
input_linked_list = create_linked_list(head)
result_linked_list = solution.reverseBetween(input_linked_list, left, right)
print_linked_list(result_linked_list) # [1, 4, 3, 2, 5]

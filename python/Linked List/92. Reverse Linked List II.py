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

        root = ListNode(None)
        root.next = head
        prev = root

        # go to the starting and ending points
        for _ in range(left - 1):
            prev = prev.next
        curr = prev.next

        # # iteratively change the nodes
        # for _ in range(right - left):
        #     temp, prev.next, curr.next = prev.next, curr.next, curr.next.next
        #     prev.next.next = temp

        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return root.next

# Test case
solution = Solution()
head = [1,2,3,4,5]
left = 2; right = 4
input_linked_list = create_linked_list(head)
result_linked_list = solution.reverseBetween(input_linked_list, left, right)
print_linked_list(result_linked_list) # [1, 4, 3, 2, 5]

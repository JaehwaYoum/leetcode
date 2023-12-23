# 328. Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/

# Date: Dec 23, 2023
# Difficulty: Medium

from linkedlist import *
# Solution
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head
        return head

# Test case
solution = Solution()
head = [2,1,3,5,6,4,7]
input_linked_list = create_linked_list(head)
result_linked_list = solution.oddEvenList(input_linked_list)
print_linked_list(result_linked_list) # [2, 3, 6, 7, 1, 5, 4]

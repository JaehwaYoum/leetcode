# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Date: Dec 27, 2023
# Difficulty: Medium

from linkedlist import *

# Solution
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = head = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            sum = 0

            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next


# Test case
solution = Solution()
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
input_list_1 = create_linked_list(l1)
input_list_2 = create_linked_list(l2)
result_linked_list = solution.addTwoNumbers(input_list_1, input_list_2)
print_linked_list(result_linked_list) # [8, 9, 9, 9, 0, 0, 0, 1]

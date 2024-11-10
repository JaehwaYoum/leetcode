# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Date: Nov 9, 2024
# Difficulty: Medium

from linkedlist import *

# Solution
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        root = ListNode(0, next=head)
        left, right = root, head

        for _ in range(n):
            right = right.next

        while right is not None:
            left, right = left.next, right.next

        left.next = left.next.next
        return root.next


# Test case
solution = Solution()
head = [1,2,3,4,5]
n = 2
input_list = create_linked_list(head)
result_linked_list = solution.removeNthFromEnd(input_list, n)
print_linked_list(result_linked_list) # [1, 2, 3, 5]

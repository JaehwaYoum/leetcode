# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/

# Date: Jul 6, 2024
# Difficulty: Easy
from linkedlist import *

# Solution
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Floyd's cycle detection
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        # Loop until fast or fast.next is None (no cycle) or slow meets fast (cycle detected)
        while fast and fast.next:
            if slow == fast:
                return True

            slow = slow.next
            fast = fast.next.next

        return False


    # Test case
solution = Solution()
head = [3,2,0,-4]
input_linked_list = create_linked_list(head)
result = solution.hasCycle(input_linked_list)
print(result) # False
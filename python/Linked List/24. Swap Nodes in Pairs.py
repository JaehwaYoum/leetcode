# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/

# Date: Dec 23, 2023
# Difficulty: Medium

from linkedlist import *

# Solution 1: change the values
class Solution1(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        return head

# Solution 2: iterative
class Solution2(object):
    def swapPairs(self, head):
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            # swaps head and head.next (now b -> head)
            b = head.next
            head.next = b.next
            b.next = head

            # make prev point to b (now prev -> b -> head)
            prev.next = b

            # move on for next comparison
            head = head.next
            prev = prev.next.next

        return root.next

# Solution 3: recursive
class Solution3(object):
    def swapPairs(self, head):
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head

# Test case
solution = Solution3()
head = [1,2,3,4]
input_linked_list = create_linked_list(head)
result_linked_list = solution.swapPairs(input_linked_list)
print_linked_list(result_linked_list) # [2, 1, 4, 3]


# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

# Date: Dec 27, 2023
# Difficulty: Easy

from linkedlist import *

# Solution 1: recursive
# Time: O(n), Space: O(n)
class Solution1(object):
    def reverseList(self, head):
        def reverse(node, prev=None):
            if not node:
                return prev

            next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head)


# Solution 2: iterative
# Time: O(n), Space: O(1)
class Solution2(object):
    def reverseList(self, head):
        prev, node = None, head

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev


# Test case
solution = Solution1()
head = [1,2,3,4,5]
input_linked_list = create_linked_list(head)
result_linked_list = solution.reverseList(input_linked_list)
print_linked_list(result_linked_list) # [5, 4, 3, 2, 1]

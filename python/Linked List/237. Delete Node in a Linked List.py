# 237. Delete Node in a Linked List
# https://leetcode.com/problems/delete-node-in-a-linked-list/description/

# Date: Nov 9, 2024
# Difficulty: Medium

from linkedlist import *

# Solution
# Time: O(1), Space: O(1)
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val, node.next = node.next.val, node.next.next 


# Test case
solution = Solution()
head = [4,5,1,9]
node = 5 # This is the node with value 5

input_linked_list = create_linked_list(head)
solution.deleteNode(input_linked_list.next)
print_linked_list(input_linked_list) # [4, 1, 9]

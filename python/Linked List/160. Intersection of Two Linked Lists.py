# 160. Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Date: Jul 6, 2024
# Difficulty: Easy

from linkedlist import create_linked_list, print_linked_list
# Solution
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        # function to return the length of a linked list
        def get_length(node):
            length = 0
            while node:
                node = node.next
                length += 1
            return length

        lenA = get_length(headA)
        lenB = get_length(headB)

        # move the head until lengths of two lists are the same
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        while lenA < lenB:
            headB = headB.next
            lenB -= 1

        # return the first identical value (intersection)
        while headA and headB:
            if headA.val == headB.val:
                return headA
            headA = headA.next
            headB = headB.next

        return None


# Test case
solution = Solution()
listA = [1, 9, 1, 2, 4]; listB = [3, 2, 4]
listA_head= create_linked_list(listA)
listB_head = create_linked_list(listB)
result_linked_list = solution.getIntersectionNode(listA_head, listB_head)
print_linked_list(result_linked_list) # [2, 4]
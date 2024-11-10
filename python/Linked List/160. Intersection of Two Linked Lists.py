# 160. Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Date: Nov 9, 2024
# Difficulty: Easy

# Solution
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def getLength(node):
            len = 0
            while node:
                len += 1
                node = node.next
            return len

        lenA = getLength(headA)
        lenB = getLength(headB)

        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        while lenB > lenA:
            lenB = lenB.next
            lenB -= 1

        while headA and headB:
            if headA == headB:
                return headA
            headA, headB = headA.next, headB.next

        return None

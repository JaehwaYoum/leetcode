# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/

# Date: Oct 5, 2023
# Difficulty: Easy

from linkedlist import *

# Solution
# Time: O(n), Space: O(n)
import collections
class Solution1(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        p = head
        q = collections.deque()

        while p:
            q.append(p.val)
            p = p.next

        while q:
            if len(q) == 1:
                return True
            if q.popleft() != q.pop():
                return False

        return True

class Solution2(object):
    def isPalindrome(self, head):
        p = head
        lst = []

        while p:
            lst.append(p.val)
            p = p.next

        return lst == lst[::-1]


# Test case
solution = Solution2()
head = [1,2,2,1]
input_linked_list = create_linked_list(head)
result = solution.isPalindrome(input_linked_list)
print(result) # True

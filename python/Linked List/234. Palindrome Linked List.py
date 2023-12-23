# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/

# Date: Oct 5, 2023
# Difficulty: Easy

from linkedlist import *

# Solution
# Time: O(n), Space: O(n)
import collections
class Solution(object):
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
            if q.popleft() != q.pop():
                return False

        return True

# Test case
solution = Solution()
head = [1,2,2,1]
input_linked_list = create_linked_list(head)
result = solution.isPalindrome(input_linked_list)
print(result) # True

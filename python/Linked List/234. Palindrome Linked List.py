# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/

# Date: Oct 5, 2023
# Difficulty: Easy

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


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Test case
solution = Solution()
head = [1,2,2,1]
input_linked_list = create_linked_list(head)
result = solution.isPalindrome(input_linked_list)
print(result) # True

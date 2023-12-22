# 147. Insertion Sort List
# https://leetcode.com/problems/insertion-sort-list/

# Date: Nov 28, 2023
# Difficulty: Medium

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution
# Time: O(n^2), Space: O(1)
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            # check whether to reset cur to the start of the sorted list (parent).
            if head and cur.val > head.val:
                cur = parent

        return parent.next


# Test case

# Utility function to create a linked list from an array
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Utility function to change the linked list to an array
def linked_list_to_array(head):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr

# Create the linked list
head = create_linked_list([4, 2, 1, 3])

solution = Solution()
sorted_head = solution.insertionSortList(head)

# Print the sorted linked list
sorted_array = linked_list_to_array(sorted_head)
print(sorted_array)
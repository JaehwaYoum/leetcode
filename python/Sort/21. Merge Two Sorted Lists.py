# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# Date: Sep 24, 2023
# Difficulty: Easy

# Time: O(n), Space: O(n)

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)

        return list1

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

def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# Test case
solution = Solution()
list1 = [1,2,4]
list2 = [1,3,4]

linked_list1 = create_linked_list(list1)
linked_list2 = create_linked_list(list2)
result_linked_list = solution.mergeTwoLists(linked_list1, linked_list2)
print_linked_list(result_linked_list)  # [1, 1, 2, 3, 4, 4]
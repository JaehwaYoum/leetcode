# 148. Sort List
# https://leetcode.com/problems/sort-list/

# Date: Sep 30, 2023
# Difficulty: Medium

# Solution 1: convert to list and then back to linked list
# Time: O(n*log(n)), Space: O(n)
class Solution1(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        lst = []
        while p:
            lst.append(p.val)
            p = p.next

        lst.sort()

        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head

# Solution 2: merge sort
# Time: O(n*log(n)), Space: O(log(n))
class Solution2(object):
    def sortList(self, head):
        def MergeTwoLists(l1, l2):
            if l1 and l2:
                if l1.val > l2.val:
                    l1, l2 = l2, l1
                l1.next = MergeTwoLists(l1.next, l2)
            return l1 or l2

        if not (head and head.next):
            return head

        # split the linked list into two halves
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        # recursively sort the separated lists
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        # return the merged lists
        return MergeTwoLists(l1, l2)


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
head = [-1,5,3,4,0]
input_linked_list = create_linked_list(head)
result_linked_list = solution.sortList(input_linked_list)
print_linked_list(result_linked_list) # [-1, 0, 3, 4, 5]
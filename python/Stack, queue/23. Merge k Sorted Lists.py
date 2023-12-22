# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

# Date: Dec 13, 2023
# Difficulty: Hard

import heapq
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        root = result = ListNode(None)
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next


# Utility functions for test case
def array_to_linked_list(arr):
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_array(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

# Test case
lists = [[1,4,5],[1,3,4],[2,6]]

linked_lists = [array_to_linked_list(l) for l in lists]

solution = Solution()
merged_list_head = solution.mergeKLists(linked_lists)

output = linked_list_to_array(merged_list_head)
print(output) # [1, 1, 2, 3, 4, 4, 5, 6]
# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Date: Nov 9, 2024
# Difficulty: Easy

from linkedlist import *

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy 

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2
        return dummy.next

        
# Test case
solution = Solution()
list1 = [1,2,4]
list2 = [1,3,4]
input_linked_list_1 = create_linked_list(list1)
input_linked_list_2 = create_linked_list(list2)
result_linked_list = solution.mergeTwoLists(input_linked_list_1, input_linked_list_2)
print_linked_list(result_linked_list) # [1, 1, 2, 3, 4, 4]


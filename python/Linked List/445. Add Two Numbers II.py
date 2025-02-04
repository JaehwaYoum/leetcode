# 445. Add Two Numbers II
# https://leetcode.com/problems/add-two-numbers-ii/

# Date: Feb 3, 2025
# Difficulty: Medium

from linkedlist import *

# Solution 1: Combine 206. Reverse and 2. Add Two Numbers I 
# Time: O(n + m), Space: O(max(n, m)) (n: length of l1, m: length of l2)
class Solution1(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # reverse the lists first
        def reverse(l):
            prev, node = None, l
            while node:
                temp = node.next
                node.next = prev
                prev, node = node, temp
            return prev

        rev_l1, rev_l2 = reverse(l1), reverse(l2)

        # do the calculations
        def add(l1, l2):
            carry, head = 0, ListNode()
            result = head

            while l1 or l2 or carry:
                temp_sum = 0

                if l1:
                    temp_sum += l1.val
                    l1 = l1.next
                if l2:
                    temp_sum += l2.val
                    l2 = l2.next
                
                carry, val = divmod(temp_sum + carry, 10)
                result.next = ListNode(val)
                result = result.next
            
            return head.next
        
        added = add(rev_l1, rev_l2)

        # reverse the result again 
        return reverse(added)


# Solution 2: Stack
# Time: O(n + m), Space: O(n + m)
class Solution2(object):
    def addTwoNumbers(self, l1, l2):

        stack1, stack2 = [], []
        carry, head = 0, None
        result = head

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            
            carry, val = divmod(carry + val1 + val2, 10)
            node = ListNode(val, result) # keeps updating to the latest head of the linked list
            result = node
        
        return node



# Test case
solution = Solution()
l1 = [7,2,4,3]; l2 = [5,6,4]
input_list_1 = create_linked_list(l1)
input_list_2 = create_linked_list(l2)
result_linked_list = solution.addTwoNumbers(input_list_1, input_list_2)
print_linked_list(result_linked_list) # [7, 8, 0, 7]

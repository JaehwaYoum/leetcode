# 496. Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/description/

# Date: Jul 6, 2024
# Difficulty: Easy

# Solution 1
class Solution1(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        nums1 and nums2 are distinct 0-indexed integer arrays, where nums1 is a subset of nums2.
        """

        # dictionary to store the next greater element
        next_elements = {}

        for i in range(len(nums2)):
            next_element = -1 # value to store when there are none

            for j in range(i+1, len(nums2)):
                if nums2[i] < nums2[j]:
                    next_element = nums2[j]
                    break # break the loop when the next greater element is found
            next_elements[nums2[i]] = next_element

        return [next_elements[num] for num in nums1]


# Solution 2: stack
class Solution2(object):
    def nextGreaterElement(self, nums1, nums2):

        next_elements = {}
        stack = [nums2[0]]

        for i in range(1, len(nums2)):
            # when we found a pair, keep popping from stack until the top of stack is smaller than current number
            if stack[-1] < nums2[i]:
                next_elements[stack[-1]] = nums2[i]
                stack.pop()

            # after matching pairs are found, push the current element to the stack
            stack.append(nums2[i])

        # after we finished traversing nums2, the elements in the stack didn't have greater elements
        for element in stack:
            next_elements[element] = -1

        return [next_elements[num] for num in nums1]


# Test case
solution = Solution2()
nums1 = [4,1,2]; nums2 = [1,3,4,2]

result = solution.nextGreaterElement(nums1, nums2)
print(result) # [-1,3,-1]
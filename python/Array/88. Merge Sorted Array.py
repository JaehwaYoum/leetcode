# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/description/

# Date: Jan 27, 2024
# Difficulty: Easy

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]

        else:
            for i in range(n):
                nums1[i + m] = nums2[i]
            nums1.sort()

        return nums1

# Test case
solution = Solution()

nums1 = [1,2,3,0,0,0]; m = 3
nums2 = [2,5,6]; n = 3
result = solution.merge(nums1, m, nums2, n)
print(result) # [1, 2, 2, 3, 5, 6]
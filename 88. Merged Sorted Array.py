# 88. Merged Sorted Array.py
# https://leetcode.com/problems/merge-sorted-array/

# Date: Jul 02, 2023
# Difficulty: Easy

# Time: O(n*log(n))
# Space: O(1)

# Solution 1
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        nums1[m:] = nums2
        nums1.sort()

        return nums1

# Test case
solution = Solution()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
result = solution.merge(nums1, m, nums2, n)
print(result)

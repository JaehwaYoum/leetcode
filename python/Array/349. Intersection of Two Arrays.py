# 349. Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/

# Date: Nov 28, 2023
# Difficulty: Easy

# Solution 1: bisect
# Time: O(n), Space: O(1)
import bisect
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        result = set()
        nums2.sort()

        for n1 in nums1:
            i2 = bisect.bisect_left(nums2, n1)
            if len(nums2) and len(nums2) > i2 and n1 == nums2[i2]:
                result.add(n1)

        return result

# Solution 2: insertion sort
# Time: O(), Space: O()
class Solution2(object):
    def intersection(self, nums1, nums2):
        result = set()

        nums1.sort()
        nums2.sort()
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1

        return result


# Test case
solution = Solution2()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
result = solution.intersection(nums1, nums2)
print(result) #{9, 4}
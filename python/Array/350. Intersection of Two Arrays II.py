# 350. Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii

# Date: Oct 11, 2024
# Difficulty: Easy

class Solution(object):
    def intersect(self, nums1, nums2):
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
solution = Solution()
nums1 = [1,2,2,1]
nums2 = [2, 2]
result = solution.intersect(nums1, nums2)
print(result) # [2, 2]
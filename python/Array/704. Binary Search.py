# 704. Binary Search
# https://leetcode.com/problems/binary-search/

# Date: Nov 22, 2023
# Difficulty: Easy

# Solution 1: recursive function
# Time: O(log(n)), Space: O(log(n))
class Solution1(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def binarySearch(start, end):
            if start <= end:
                mid = (start + end) // 2
                # to prevent overflow, mid = start + (end-start) // 2
                if nums[mid] < target:
                    return binarySearch(mid+1, end)
                elif nums[mid] > target:
                    return binarySearch(start, mid-1)
                else:
                    return mid
            else:
                return -1
        return binarySearch(0, len(nums)-1)

# Solution 2: bisect module
# Time: O(log(n)), Space: O(1)
import bisect
class Solution2(object):
    def search(self, nums, target):
        index = bisect.bisect_left(nums, target)
        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1

# Solution 3: simplified linear search
# Time: O(n), Space: O(1)
class Solution3(object):
    def search(self, nums, target):
        try:
            return nums.index(target)
        except ValueError:
            return -1


# Test case
solution = Solution2()

nums = [-1,0,3,5,9,12]
target = 9
result = solution.search(nums, target)
print(result) # 4
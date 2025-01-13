# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

# Date: Nov 22, 2023
# Difficulty: Medium

# Solution 1: 2-step binary search
# Time: O(log n), Space: O(1)
class Solution1(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        # step 1: find the pivot
        left, right = 0, len(nums)-1
        # exit the loop when left >= right
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        # step 2: find the target index in respect to the pivot
        left, right = 0, len(nums) - 1
        # left=right allows to check the middle element one last time
        while left <= right:
            mid = left + (right - left) // 2
            # shifts the mid to the pivot, and ensures the index is in the bounds of the original array
            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
        return -1


# Solution 2: 1-step binary search
# Time: O(log n), Space: O(1)
class Solution2(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # check if left subarray is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # check if right subarray is sorted
            if nums[mid] <= nums[right]:
                if nums[mid] <= target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


# Solution 3: Simplified linear search
# Time: O(n), Space: O(1)
class Solution3(object):
    def search(self, nums, target):
        try:
            tar_index = nums.index(target)
            return tar_index
        except ValueError:
            return -1


# Test case
solution = Solution2()

nums = [4,5,6,7,0,1,2]
target = 0
result = solution.search(nums, target)
print(result) # 4
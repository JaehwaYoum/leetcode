# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Date: Nov 10, 2024
# Difficulty: Medium

# Time: O(log n), Space: O(1)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = self.binary_search(nums, target, is_left=True)
        end = self.binary_search(nums, target, is_left=False)
        return [start, end]

    
    def binary_search(self, nums, target, is_left):
        i, j = 0, len(nums)-1
        result = -1 # if not found, we return -1 

        while i < j:
            mid = i + (j-i) // 2

            if nums[mid] == target:
                result = mid

                if is_left:
                    j = mid
                else:
                    i = mid + 1
            elif nums[mid] > target:
                j = mid
            else:
                i = mid + 1

        return result        


# Test case
solution = Solution()

nums = [5,7,7,8,8,10]
target = 8
result = solution.search(nums, target)
print(result) # [3,4]
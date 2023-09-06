# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/

# Date: Aug 30, 2023
# Difficulty: Medium

# Solution 1
# Time: O(n), Space: O(1)
class Solution1(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        steps = k%length

        nums[:] = nums[-steps:] + nums[:-steps]

# Solution 2 (copy array)
# Time: O(n), Space: O(n)
class Solution2(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        copy = [nums for nums in nums]
        length = len(nums)

        for i in range(length):
            nums[(i+k)%length] = copy[i]

# Solution 3 (append and remove, time limit exceeded)
# Time: O(n*k), Space: O(1)
class Solution3(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        steps = length-k if length>k else length-k%length

        for i in range(steps):
            nums.append(nums[i])
        for j in range(steps):
            nums.remove(nums[0])

# Test case
solution = Solution2()

nums = [1,2,3,4,5,6,7]
k = 3
solution.rotate(nums, k)
print(nums)
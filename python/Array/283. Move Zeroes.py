# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/

# Date: Sep 24, 2023
# Difficulty: Easy

# Solution 1: Two Pointers
# Time: O(n), Space: O(1)
class Solution1(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        nonzero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nonzero] = nums[i]
                nonzero += 1

        for i in range(nonzero, len(nums)):
            nums[i] = 0


# Solution 2: Pop and append 
# Time: O(n^2), Space: O(n)
class Solution1(object):
    def moveZeroes(self, nums):
        zeros = []
        i = len(nums) - 1

        while i >= 0:
            if nums[i] == 0:
                num = nums.pop(i)
                zeros.append(num)
            i -= 1

        nums.extend(zeros)


# Solution 3: Pop and append 
# Time: O(n^2), Space: O(n)
class Solution1(object):
    def moveZeroes(self, nums):
        cnt = 0
        for num in nums:
            if num == 0:
                cnt += 1

        for i in range(cnt):
            nums.remove(0)

        nums.extend([0] * cnt)



# Test case : in-place without making a copy of the array.
solution = Solution1()

nums = [0,1,0,3,12]
solution.moveZeroes(nums)
print(nums) # [1, 3, 12, 0, 0]
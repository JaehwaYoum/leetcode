# 1752. Check if Array Is Sorted and Rotated
# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

# Date: Feb 2, 2025
# Difficulty: Easy

# Solution 1: Brute Force
# Time: O(n), Space: O(1)
class Solution1(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt, n = 0, len(nums)
        prev = nums[0]

        for i in range(1, n):
            if prev > nums[i]:
                cnt += 1
            prev = nums[i]
            if i == n - 1 and nums[0] < nums[i]:
                cnt += 1
            if cnt > 1:
                return False
        return True


# Solution 2: Circular comparison using modulo
# Time: O(n), Space: O(1)
class Solution2(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt, n = 0, len(nums)
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                cnt += 1
                if cnt > 1:
                    return False
        return True


# Test case
solution = Solution2()

nums = [2,1,3,4]
result = solution.check(nums)

print(result) # False
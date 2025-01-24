# 41. First Missing Positive
# https://leetcode.com/problems/first-missing-positive/description/

# Date: Feb 25, 2024
# Difficulty: Hard

# Time: O(n), Space: O(1) (modifies in-place)
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        for i in range(n):
            # check if the element is in the valid array
            # and if the element is in the correct position
            while 1 <= nums[i] <= n-1 and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                # cf) nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
                # is wrong because nums[i] is repeatedly being placed in the wrong index

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


# Test case
solution = Solution()

nums = [7,8,9,11,12]
result = solution.firstMissingPositive(nums)
print(result)  # 1
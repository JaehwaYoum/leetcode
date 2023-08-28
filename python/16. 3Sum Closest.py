# 16. 3Sum Closest
# https://leetcode.com/problems/3sum-closest/

# Date: Aug 27, 2023
# Difficulty: Medium

# Time: O(n^2)
# Space: O(1)

# Solution 1
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort() # sort the list, Time complexity O(n*log(n))
        closest_sum = 10 ** 5  # large number (-10**4 <= target <= 10**4)

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # if current_sum gets closer to target, update closest_sum
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                # if current_sum is same as target, return current_sum
                if current_sum == target:
                    return current_sum

                # while current_sum is not the same as target
                # move the left and right pointers to find the closest sum
                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum

# Test case
solution = Solution()

nums = [-1,2,1,-4]
target = -1
result = solution.threeSumClosest(nums, target)
print(result)
# -1
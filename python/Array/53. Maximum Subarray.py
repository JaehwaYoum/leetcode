# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

# Date: Jul 12, 2023
# Difficulty: Medium

# Solution 1
# Time: O(n), Space: O(1)
class Solution1(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        currentsum = 0
        maxsum = float('-inf')
        startindex = 0
        endindex = -1

        # Update current sum by adding the current element
        for i in range(len(nums)):
            if currentsum < 0:
                currentsum = nums[i]
                startindex = i
            else:
                currentsum += nums[i]

            # Check if the current sum is greater than the maximum sum
            if currentsum > maxsum:
                maxsum = currentsum
                endindex = i

        return maxsum

# Solution 2: simplified
# Time: O(n), Space: O(1)
class Solution2(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(1, len(nums)):
            nums[i] += nums[i-1] if nums[i-1]>0 else 0
        return max(nums)

# Solution 3: Kadane algorithm
# Time: O(n), Space: O(1)
class Solution3(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        best_sum = float('-inf')
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        return best_sum


# Test case
solution = Solution3()

nums = [-2,1,-3,4,-1,2,1,-5,4]
result = solution.maxSubArray(nums)
print(result)
# 6
# The subarray [4,-1,2,1] has the largest sum 6.
# 485. Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones

# Date: Nov 9, 2024
# Difficulty: Easy

# Solution 1
# Time: O(n), Space: O(1)
class Solution1(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        curr_result = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                curr_result += 1
                result = max(result, curr_result)
            else:
                curr_result = 0      
            
        return result 

# Solution 2: Sliding Window (faster)
# Time: O(n), Space: O(1)
class Solution2(object):
    def findMaxConsecutiveOnes(self, nums):
        result, windowSize = 0, 0

        for n in nums:
            if n == 1:
                windowSize += 1
            else:
                result = max(result, windowSize)
                windowSize = 0

        return max(result, windowSize)


# Test case
solution = Solution1()
nums = [1,1,0,1,1,1]
result = solution.findMaxConsecutiveOnes(nums)
print(result) 

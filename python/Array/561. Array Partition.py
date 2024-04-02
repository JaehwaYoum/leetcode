# 561. Array Partition
# https://leetcode.com/problems/array-partition/description/

# Date: Nov 1, 2023
# Difficulty: Easy

# Solution 1
# Time: O(n log n), Space: O(n)
class Solution1(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = sum([nums[i] for i in range(0, len(nums), 2)])
        return result

# Time: O(n log n), Space: O(n)
# Solution 2
class Solution2(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return sum(sorted(nums)[::2])


# Test case
solution = Solution2()

nums = [6,2,6,5,1,2]
result = solution.arrayPairSum(nums)
print(result)
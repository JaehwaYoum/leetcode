# 905. Sort Array By Parity
# https://leetcode.com/problems/sort-array-by-parity/description/

# Date: Apr 12, 2024
# Difficulty: Easy

# Solution 1: list comprehension
class Solution1(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        return [x for x in nums if x%2==0] + [x for x in nums if x%2!=0]

# Solution 2: two pointers
class Solution2(object):
    def sortArrayByParity(self, nums):
        i, j = 0, len(nums) - 1
        while i < j:
            if (nums[i] % 2 == 1) and (nums[j] % 2 == 0):
                nums[i], nums[j] = nums[j], nums[i]

            if nums[i] % 2 == 0:
                i += 1
            if nums[j] % 2 == 1:
                j -= 1
        return nums

# Solution 3: queue
import collections
class Solution3(object):
    def sortArrayByParity(self, nums):
        queue = collections.deque()

        for num in nums:
            if num % 2 == 0:
                queue.appendleft(num)
            else:
                queue.append(num)
        return list(queue)


# Test case
solution = Solution2()

nums = [3,1,2,4]
result = solution.sortArrayByParity(nums)
print(result)
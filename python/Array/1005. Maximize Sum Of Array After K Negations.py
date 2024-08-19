# 1005. Maximize Sum Of Array After K Negations
# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/

# Date: Aug 17, 2024
# Difficulty: Easy

# Solution
class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
        while k > 0:
            minimum = heapq.heappop(heap)
            heapq.heappush(heap, -minimum)
            k -= 1
        return sum(heap)

# Test case
solution = Solution()
nums = [4,2,3]; k = 1		
result = solution.largestSumAfterKNegations(nums, k)
print(result)
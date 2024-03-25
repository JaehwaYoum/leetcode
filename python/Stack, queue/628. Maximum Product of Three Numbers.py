# 628. Maximum Product of Three Numbers
# https://leetcode.com/problems/maximum-product-of-three-numbers/description/

# Date: Feb 9, 2024
# Difficulty: Easy

# Solution: Heap
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        min_heap = heapq.nsmallest(2, nums)
        max_heap = heapq.nlargest(3, nums)

        return max(max_heap[0] * max_heap[1] * max_heap[2],
                max_heap[0] * min_heap[0] * min_heap[1])

# Test case
solution = Solution()
nums = [-1,-2,-3]
result = solution.maximumProduct(nums)
print(result) # -6

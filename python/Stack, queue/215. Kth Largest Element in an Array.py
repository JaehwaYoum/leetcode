# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/

# Date: Dec 18, 2023
# Difficulty: Medium

# Solution 1
import heapq
class Solution1(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)

        for _ in range(k - 1):
            heapq.heappop(heap)

        return -heapq.heappop(heap)

# Solution 2
class Solution2(object):
    def findKthLargest(self, nums, k):
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)

# Solution 3
class Solution3(object):
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

# Solution 4
class Solution4(object):
    def findKthLargest(self, nums, k):
        return sorted(nums, reverse=True)[k-1]


# Test case
solution = Solution1()
nums = [3,2,3,1,2,4,5,5,6]
k = 4

result = solution.findKthLargest(nums, k)
print(result) # 4


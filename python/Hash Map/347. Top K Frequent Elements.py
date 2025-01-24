# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

# Date: Dec 18, 2023
# Difficulty: Medium

# Solution 1
import heapq
class Solution1(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = collections.Counter(nums)
        freq_heap = []

        for f in freq:
            heapq.heappush(freq_heap, (-freq[f], f))

        topk = list()
        for _ in range(k):
            topk.append(heapq.heappop(freq_heap)[1])

        return topk

# Solution 2
import collections
class Solution2(object):
    def topKFrequent(self, nums, k):
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
        # * is for unpacking
        # list(zip()): zip returns generator, list makes it mutable


# Test case
solution = Solution1()
nums = [1,1,1,2,2,3]
k = 2
result = solution.topKFrequent(nums, k)
print(result) # [1,2]

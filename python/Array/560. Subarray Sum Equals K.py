# 560. Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/
import collections


# Date: Jan 5, 2025
# Difficulty: Medium

# Solution 1: Sliding Window
# Time: O(n^2), Space: O(1)
class Solution1(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        result = 0
        i, j = 0, 0

        # edge case
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return int(nums[0] == k) # Change boolean to integer

        while j < len(nums):
            subsum = sum(nums[i:j+1])
            if subsum == k:
                result += 1
                j += 1
            elif subsum < k:
                j += 1
            else:
                i += 1

        return result


# Solution 2: Prefix Hashmap
# Time: O(n), Space: O(n)
class Solution2(object):
    def subarraySum(self, nums, k):
        d = collections.defaultdict(int)
        d[0] = 1
        prefix_sum = 0
        result = 0

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in d:
                result += d[prefix_sum - k]
            # elif prefix_sum == k:  --- this case is covered by the if clause
            #     result += 1

            d[prefix_sum] += 1
        
        return result


# Test case
solution = Solution2()

nums = [1, -1, 0]
k = 0
result = solution.subarraySum(nums, k)
print(result) # 3
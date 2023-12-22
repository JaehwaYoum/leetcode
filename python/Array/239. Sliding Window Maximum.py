# 239. Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum/

# Date: Dec 18, 2023
# Difficulty: Hard

# Solution 1: Brute Force (TLE)
class Solution1(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if not nums:
            return nums

        r = []
        for i in range(len(nums) - k + 1):
            r.append(max(nums[i:i + k]))

        return r

# Solution 2: Queue (TLE)
import collections
class Solution2(object):
    def maxSlidingWindow(self, nums, k):

        results = []
        window = collections.deque()
        current_max = float('-inf')
        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue

            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v

            results.append(current_max)

            if current_max == window.popleft():
                current_max = float('-inf')

        return results

# Solution 3: track the index of max element using list
class Solution3(object):
    def maxSlidingWindow(self, nums, k):

        n = len(nums)
        seen = []
        result = []
        for i in range(n):
            # checks the first element in 'seen' corresponds to an index that is outside the current sliding window
            if seen and seen[0] == i - k:
                seen.pop(0) # removes and returns the first element from the list

            # new element is larger than the previous maximum (nums[seen[-1]])
            while seen and nums[seen[-1]] < nums[i]:
                seen.pop() # removes and returns the last element from the list

            seen.append(i)

            # when the window size reaches k or more, append the max value to ans list
            if i >= k - 1:
                result.append(nums[seen[0]])

        return result


# Test case
solution = Solution3()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
result = solution.maxSlidingWindow(nums, k)
print(result) # [3,3,5,5,6,7]
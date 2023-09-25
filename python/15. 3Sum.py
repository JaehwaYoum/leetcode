# 15. 3Sum
# https://leetcode.com/problems/3sum/

# Date: Sep 24, 2023
# Difficulty: Medium

# Time: O(n^2), Space: O(n^2)
# Solution 1
class Solution1(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = set()

        n, p, z = [], [], []

        for num in nums:
            if num > 0:
                p.append(num)
            if num < 0:
                n.append(num)
            if num == 0:
                z.append(num)

        N, P = set(n), set(p)

        if len(z) > 2:
            res.add((0, 0, 0))

        if z:
            for pnum in P:
                if -1 * pnum in N:
                    res.add((-1 * pnum, 0, pnum))

        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -1 * (n[i] + n[j])
                if target in P:
                    res.add(tuple(sorted([n[i], n[j], target])))

        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -1 * (p[i] + p[j])
                if target in N:
                    res.add(tuple(sorted([target, p[i], p[j]])))

        res = [list(r) for r in res]

        return res

# Time: O(n^2), Space: O(n^2)
# Solution 2
class Solution2(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            # skip when the same number appears
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # calculate the sum using two pointers
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    results.append((nums[i], nums[left], nums[right]))

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results
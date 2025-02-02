# 2289. Steps to Make Array Non-decreasing
# https://leetcode.com/problems/steps-to-make-array-non-decreasing/

# Date: Feb 2, 2025
# Difficulty: Medium

# Solution 1: TLE
# Time: O(n^2), Space: O(n)
class Solution1(object):
    def totalSteps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        while nums: # nested iteration 
            num_pop, idx = 0, 0
            temp_nums = []
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    temp_nums.extend(nums[idx:i+1])
                    idx = i + 2
                    num_pop +=1
            temp_nums.extend(nums[idx:])
            nums = temp_nums
            result += 1
            if num_pop == 0:
                break

        return result - 1


# Solution 2: Stack
# Time: O(n), Space: O(n)
class Solution2(object):
    def totalSteps(self, nums):
        stack, result = [], 0 # stack: [num, steps]

        for num in nums:
            steps = 0
            while stack and num >= stack[-1][0]:
                steps = max(steps, stack[-1][1])
                stack.pop()

            if stack:
                steps += 1
            else:
                steps = 0

            stack.append([num, steps]) # [5, 0] -> [7, 3] -> [11, 3] -> [11, 3]
            result = max(result, steps)

        return result


# Solution 3: DP
# Time: O(n), Space: O(n)
class Solution3(object):
    def totalSteps(self, nums):
        dp = [0] * len(nums) # stores steps 
        stack = [] # stores index

        for i in range(len(nums)):
            steps = 0
            while stack and nums[i] >= nums[stack[-1]]:
                steps = max(steps, dp[stack[-1]])
                stack.pop()

            if stack:
                dp[i] = steps + 1
            stack.append(i) # [0] -> [0, 1] -> [0, 2] -> [0, 3] -> [4] -> ...
        return max dp



# Test case
solution = Solution2()

nums = [5,3,4,4,7,3,6,11,8,5,11]
result = solution.totalSteps(nums)

print(result) # 3
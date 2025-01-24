# 228. Summary Ranges
# https://leetcode.com/problems/summary-ranges/

# Date: Jan 23, 2025
# Difficulty: Easy

# Solution 1-1: Brute Force with temp array 
# Time: O(n), Space: O(n)
class Solution1_1(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """    
        if not nums:
            return []

        temp, result = [str(nums[0])], []

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                if i == len(nums) - 1 or nums[i] + 1 != nums[i + 1]:
                    result.append(temp.pop() + "->" + str(nums[i]))
            else:
                result.append(temp.pop())
                temp.append(str(nums[i]))

        if temp:
            result.append(temp.pop())

        return result


# Solution 1-2: single variable (less overhead)
class Solution1_2(object):
    def summaryRanges(self, nums):
        if not nums:
            return []

        start, result = nums[0], []

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1: # sequence breaks 
                result.append(str(start) if start == nums[i-1] else str(start) + "->" + str(nums[i-1]))
                start = nums[i]
            
        # handle the last remaining range or single number 
        result.append(str(start) if start == nums[-1] else str(start) + "->" + str(nums[-1]))

        return result


# Solution 2: Simplified solution 
# Time: O(n), Space: O(n)
class Solution2(object):
    def summaryRanges(self, nums):
        ranges = []

        for num in nums:
            if ranges and num == ranges[-1][1] + 1:
                ranges[-1][1] = num
            else:
                ranges.append([num, num])

            # if not ranges or n > ranges[-1][-1] + 1:
            #     ranges += [],
            # ranges[-1][1:] = n,

        return [f'{x}->{y}' if x != y else f'{x}' for x, y in ranges]
        # return ['->'.join(map(str, r)) for r in ranges]



# Test case
solution = Solution2()

nums = [0,1,2,4,5,7]
result = solution.summaryRanges(nums)
print(result) # ["0->2","4->5","7"]
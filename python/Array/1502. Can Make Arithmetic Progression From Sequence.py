# 1502. Can Make Arithmetic Progression From Sequence
# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

# Date: Jan 27, 2025
# Difficulty: Easy

# Solution 1: Using sort() 
# Time: O(n log n), Space: O(1)
class Solution1(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort() 
        diff = arr[1] - arr[0]

        for i in range(len(arr) - 1):
            if diff != arr[i+1] - arr[i]:
                return False
        return True


# Solution 2: Mathematical Set 
# Time: O(n), Space: O(1)
class Solution2(object):
    def canMakeArithmeticProgression(self, arr): 
        n = len(arr)
        if n <= 2:
            return True

        minval, maxval = min(arr), max(arr)

        # check if the common difference is evenly distributed 
        if (maxval - minval) % (n - 1) != 0:
            return False

        diff = (maxval - minval) // (n - 1)
        nums_set = {minval + i * diff for i in range(n)}

        return set(arr) == nums_set



# Test case
solution = Solution2()

arr = [3,5,1]
result = solution.canMakeArithmeticProgression(arr)
print(result) # True
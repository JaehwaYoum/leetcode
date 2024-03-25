# 852. Peak Index in a Mountain Array
# https://leetcode.com/problems/peak-index-in-a-mountain-array/

# Date: Feb 25, 2024
# Difficulty: Medium

# Solution
class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        left, right = 0, len(arr)-1

        while left < right:
            mid = left + (right - left)//2
            if arr[mid] > arr[mid+1]:
                right = mid
            else:
                left = mid + 1
        
        return left

# Test case
solution = Solution()

arr = [0,10,5,2]
result = solution.peakIndexInMountainArray(arr)
print(result) # 1

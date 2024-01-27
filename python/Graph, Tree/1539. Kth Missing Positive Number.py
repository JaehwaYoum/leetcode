# 1539. Kth Missing Positive Number
# https://leetcode.com/problems/kth-missing-positive-number/description/

# Date: Jan 27, 2024
# Difficulty: Easy


class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """

        # i: strictly increasing integer, starting from 1
        # j: index of the array
        i = 1
        j = 0

        while k > 0 and j < len(arr):
            # if the number is in the array
            if arr[j] == i:
                i += 1
                j += 1

            # if not in the array, check the next number
            else:
                i += 1
                k -= 1

        # if k is still greater than 0 after the loop, add k-1 to i
        return i + k - 1


# Test case
solution = Solution()

arr = [2, 3, 4, 7, 11]
k = 5
result = solution.findKthPositive(arr, k)
print(result) # 9
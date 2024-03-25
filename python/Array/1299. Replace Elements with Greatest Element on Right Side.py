# 1299. Replace Elements with Greatest Element on Right Side
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

# Date: March 25, 2024
# Difficulty: Easy

# Solution 1
class Solution1(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        max_val = -1

        for i in range(len(arr)-1, -1, -1):
            current = arr[i]
            arr[i] = max_val

            if current > max_val:
                max_val = current

        return arr

# Solution 2: conditional assignment
class Solution2(object):
    def replaceElements(self, arr):
        temp = arr[-1]
        arr[-1] = -1

        for i in range(len(arr)-2, -1, -1):
            if arr[i] > temp:
                arr[i], temp = temp, arr[i]
            else:
                arr[i] = temp

        return arr


# Test case
solution = Solution1()

arr = [17,18,5,4,6,1]
result = solution.replaceElements(arr)
print(result) # [18,6,6,6,1,-1]

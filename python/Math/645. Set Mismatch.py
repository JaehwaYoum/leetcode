# 645. Set Mismatch
# https://leetcode.com/problems/set-mismatch/

# Date: Aug 19, 2024
# Difficulty: Easy

# Solution
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        check_set = set(range(1, n+1))
        curr_set = set(nums)
        loss_num = list(check_set.difference(curr_set))

        count_dict = collections.Counter(nums)
        rep_num = [key for key, value in count_dict.items() if value == 2]
        
        return rep_num + loss_num
# 506. Relative Ranks
# https://leetcode.com/problems/relative-ranks/description/

# Date: Jul 7, 2024
# Difficulty: Easy

# Solution 
class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """

        sorted_score = sorted(score, reverse=True)
        score_rank_list = [sorted_score.index(x) + 1 for x in score]
        rank_dict = {1: 'Gold Medal', 2: 'Silver Medal', 3: 'Bronze Medal'}
        result = [str(rank) if rank>3 else rank_dict[rank] for rank in score_rank_list]
        return result 
        

# Test case
solution = Solution()

score = [5,4,3,2,1]
result = solution.findRelativeRanks(score)
print(result) # ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5']

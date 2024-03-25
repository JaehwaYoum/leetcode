# 274. H-Index
# https://leetcode.com/problems/h-index/

# Date: Sep 3, 2023
# Difficulty: Medium

# Solution 1
# Time: O(n^2), Space: O(1)
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        papers = len(citations)
        hindex = 0

        if all(element == 0 for element in citations):
            return 0

        i = 1
        while i <= papers:
            check = i
            count = 0
            for j in range(papers):
                if citations[j] >= check:
                    count += 1
                if count >= check:
                    hindex = i
                    break
            i += 1

        return hindex

# Test case
solution = Solution()

citations = [1,3,1]
result = solution.hIndex(citations)
print(result)
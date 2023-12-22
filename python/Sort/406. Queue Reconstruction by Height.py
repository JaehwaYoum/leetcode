# 406. Queue Reconstruction by Height
# https://leetcode.com/problems/queue-reconstruction-by-height/

# Date: Nov 22, 2023
# Difficulty: Medium

# Solution
# Time: O(n^2), Space: O(n)
import heapq
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        result = []
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])

        return result


# Test case
solution = Solution()
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
result = solution.reconstructQueue(people)
print(result) # [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
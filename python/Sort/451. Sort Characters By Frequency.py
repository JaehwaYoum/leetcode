# 451. Sort Characters By Frequency
# https://leetcode.com/problems/sort-characters-by-frequency/

# Date: Nov 10, 2024
# Difficulty: Medium

import collections
# Solution 1
class Solution1(object):
    def frequencySort(self, s:str) -> str:
        counter = collections.Counter(s)
        ordered_counter = dict(sorted(counter.items(), key=lambda x:x[1], reverse=True))
        result = []

        for k in ordered_counter:
            while ordered_counter[k] > 0:
                result += k
                ordered_counter[k] -= 1
        return result

import heapq
# Solution 2: heap 
class Solution2(object):
    def frequencySort(self, s:str) -> str:
        counter = collections.Counter(s)
        pq = [(-freq, char) for char, freq in counter.items()]
        result = []

        heapq.heapify(pq)
        while pq:
            freq, char = heapq.heappop(pq)
            result += char * (-freq)
        return result


        

# Test case
solution = Solution1()

s = "tree"
result = solution.frequencySort(s)
print(result) #  "eert" or  "eetr"

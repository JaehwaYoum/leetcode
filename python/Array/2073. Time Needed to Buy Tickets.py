# 2073. Time Needed to Buy Tickets
# https://leetcode.com/problems/time-needed-to-buy-tickets/

# Date: March 25, 2024
# Difficulty: Easy

# Solution 1: Brute Force
class Solution1(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        result = 0

        while tickets[k] > 0:
            for i in range(len(tickets)):
                if tickets[i] == 0:
                    continue
                if tickets[k] == 0:
                    break
                tickets[i] -= 1
                result += 1
        return result

# Solution 2: Reduced to O(N)
class Solution2(object):
    def timeRequiredToBuy(self, tickets, k):
        result = 0

        for i in range(len(tickets)):

            if i <= k:
                # For people ahead of or at position k, all their tickets need to be counted
                result += min(tickets[i], tickets[k])

            else:
                # For people behind position k, only count up to the tickets[k] - 1 since
                # the person at k will finish buying before these people buy their last ticket
                result += min(tickets[i], tickets[k]-1)

        return result

# Test case
solution = Solution2()

tickets = [5,1,1,1]; k = 0
result = solution.timeRequiredToBuy(tickets, k)

print(result) # 25

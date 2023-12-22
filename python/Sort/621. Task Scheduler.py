# 621. Task Scheduler
# https://leetcode.com/problems/task-scheduler/description/

# Date: Nov 22, 2023
# Difficulty: Medium
import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0

            # counter.most_common(n + 1) retrieves up to n + 1 of the most common tasks
            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1

                counter.subtract(task)

                # removes tasks with zero or negative counts from the counter
                counter += collections.Counter()

            if not counter:
                break

            result += n - sub_count + 1

        return result

# Test case
solution = Solution()
tasks = ["A","A","A","B","B","B"]
n = 2
result = solution.leastInterval(tasks, n)
print(result) # 8
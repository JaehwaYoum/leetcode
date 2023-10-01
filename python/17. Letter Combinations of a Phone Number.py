# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Date: Sep 30, 2023
# Difficulty: Medium

# Time: O(4^n),Space: O(4^n) (each digit maps up to 4 letters)
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        result = []
        dials = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for i in range(index, len(digits)):
                for letter in dials[digits[i]]:
                    dfs(i+1, path+letter)

        if not digits:
            return result

        dfs(0, "")
        return result


from _collections import deque
# Time: O(n),Space: O(4^n)
class Solution2(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        dials = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        queue = deque()
        queue.append("")

        for digit in digits:
            level_size = len(queue)
            for _ in range(level_size):
                partial_combination = queue.popleft()
                for letter in dials[digit]:
                    queue.append(partial_combination+letter)

        result = list(queue)
        return result

# Recursion of lists
# Time: O(4^n),Space: O(4^n)
class Solution3(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        dials = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        queue = deque()
        queue.append("")

        all_combinations = [''] if digits else []
        for digit in digits:
            current_combinations = []
            for letter in dials[digit]:
                for combination in all_combinations:
                    current_combinations.append(combination+letter)
            all_combinations = current_combinations


        return all_combinations

# Test case
solution = Solution3()

digits = "23"
result = solution.letterCombinations(digits)
print(result)



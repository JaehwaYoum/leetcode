# 412. Fizz Buzz
# https://leetcode.com/problems/fizz-buzz/

# Date: Nov 9, 2024
# Difficulty: Easy

# Solution 1
# Time: O(n), Space: O(n)
class Solution1(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        combined_result = []

        for number in range(1, n+1):
            result = []
            if number %3 == 0:
                result.append("Fizz")
            if number %5 == 0:
                result.append("Buzz")
            if (number %3 != 0) and (number %5 != 0):
                result.append(str(number))
            combined_result.append("".join(result))
        
        return combined_result

# Solution 2: Less Overhead
# Time: O(n), Space: O(n)
class Solution2(object):
    def fizzBuzz(self, n):
        result = []

        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))

        return result

# Test case
solution = Solution1()
n = 15
result = solution.fizzBuzz(s, k)
print(result) 
# ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

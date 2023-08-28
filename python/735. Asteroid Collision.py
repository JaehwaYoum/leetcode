# 735. Asteroid Collision
# https://leetcode.com/problems/asteroid-collision/

# Date: Aug 27, 2023
# Difficulty: Medium

# Time: O(n)
# Space: O(n)

# Solution 1
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for asteroid in asteroids:

            # while loop for collisions
            # asteroids are in a row, not in the same orbit
            while stack and asteroid < 0 and stack[-1] > 0:

                # collision for same size
                if abs(asteroid) == abs(stack[-1]):
                    stack.pop()
                    break

                # collision with bigger negative value
                # goes through the while loop again
                elif abs(asteroid) > abs(stack[-1]):
                    stack.pop()

                # collision with bigger positive value
                else:
                    break

            else:
                stack.append(asteroid)

        return stack

# Test case
solution = Solution()

asteroids = [10,2,-5]
result = solution.asteroidCollision(asteroids)
print(result)
# [10]
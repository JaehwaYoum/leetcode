# 860. Lemonade Change
# https://leetcode.com/problems/lemonade-change/

# Date: Jan 29, 2025
# Difficulty: Easy

# Solution
# Time: O(n), Space: O(1)
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        received = {5: 0, 10: 0}  # track only $5 and $10 bills

        for bill in bills:
            if bill == 5:
                received[5] += 1   
                
            elif bill == 10:
                if received[5] > 0:
                    received[5] -= 1
                    received[10] += 1  
                else:
                    return False  
                
            else:  # bill == 20
                if received[10] > 0 and received[5] > 0:
                    received[10] -= 1
                    received[5] -= 1  # prefer using one $10 and one $5
                elif received[5] >= 3:
                    received[5] -= 3  
                else:
                    return False  

        return True


# Test case
solution = Solution()

bills = [5,5,10,10,20]
result = solution.lemonadeChange(bills)

print(result) # False
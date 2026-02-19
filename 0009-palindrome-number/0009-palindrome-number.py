class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 1. Negative numbers and numbers ending in 0 (except 0) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_num = 0
        original = x
        
        # 2. Reverse the number mathematically
        while x > 0:
            last_digit = x % 10
            reversed_num = (reversed_num * 10) + last_digit
            x //= 10
            
        # 3. Compare the original with the reversed version
        return original == reversed_num
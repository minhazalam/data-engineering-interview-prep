# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


# Constraints:


# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        left, right = 0, len(new_str) - 1
        while left < right:
            while left < right and not new_str[left].isalnum():
                left += 1
            while left < right and not new_str[right].isalnum():
                right -= 1
            if new_str[left] != new_str[right]:
                return False
            left += 1
            right -= 1
        return True

# 8. String to Integer (atoi)

# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:

#     Whitespace: Ignore any leading whitespace (" ").
#     Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
#     Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
#     Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.

# Return the integer as the final result.

class Solution:
    def myAtoi(self, s: str) -> int:
        sgn = 1
        temp = 0
        begin = False
        
        for i in range(len(s)):
            if s[i] == ' ' and not begin:
                continue
            if (s[i] == '-' or s[i] == '+') and not begin:
                sgn = -1 if s[i] == '-' else 1
                begin = True
                continue
            if not s[i].isdigit():
                break
            begin = True
            temp = temp * 10 + int(s[i])
            if sgn * temp > 2**31 - 1:
                return 2**31 - 1
            if sgn * temp <= -2**31:
                return -2**31
        return sgn * temp
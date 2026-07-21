# 6. Zigzag Conversion

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R

# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ""
        for i in range(numRows):
            inc = (numRows - 1) * 2
            for j in range(i, len(s), inc):
                res += s[j]
                if (i > 0 and i < numRows - 1 and j + inc - 2 * i < len(s)):
                    res += s[j + inc - 2 * i]
        return res
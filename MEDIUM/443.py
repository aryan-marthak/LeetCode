# 443. String Compression

# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

#     If the group's length is 1, append the character to s.
#     Otherwise, append the character followed by the group's length.

# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

# Note: The characters in the array beyond the returned length do not matter and should be ignored.

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        k = i = 0

        while i < n:
            chars[k] = chars[i]
            k += 1
            j = i + 1
            while j < n and chars[i] == chars[j]:
                j += 1

            if j - i > 1:
                for c in str(j - i):
                    chars[k] = c
                    k += 1
            i = j
        return k
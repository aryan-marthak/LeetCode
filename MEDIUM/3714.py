# 3714. Longest Balanced Substring II

# You are given a string s consisting only of the characters 'a', 'b', and 'c'. A of s is called balanced if all distinct characters in the substring appear the same number of times.

# Return the length of the longest balanced substring of s.

class Solution:
    def longestBalanced(self, s: str) -> int:
        # prefix counts
        a = b = c = 0
        
        # store first occurrence of each state
        first_seen = {}
        ans = 0
        
        # we must include the empty prefix
        first_seen[("abc", 0, 0)] = 0
        first_seen[("ab", 0, 0)] = 0
        first_seen[("bc", 0, 0)] = 0
        first_seen[("ca", 0, 0)] = 0
        first_seen[("a", 0, 0)] = 0
        first_seen[("b", 0, 0)] = 0
        first_seen[("c", 0, 0)] = 0
        
        for i, ch in enumerate(s, 1):
            if ch == 'a':
                a += 1
            elif ch == 'b':
                b += 1
            else:
                c += 1
            
            states = [
                ("abc", a - b, a - c),  # a = b = c
                ("ab", a - b, c),       # a = b
                ("bc", b - c, a),       # b = c
                ("ca", c - a, b),       # c = a
                ("a", b, c),            # only a
                ("b", c, a),            # only b
                ("c", a, b),            # only c
            ]
            
            for state in states:
                if state not in first_seen:
                    first_seen[state] = i
                else:
                    ans = max(ans, i - first_seen[state])
        
        return ans

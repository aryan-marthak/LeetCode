# 17. Letter Combinations of a Phone Number

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# RECURSION / BACKTRACKING 
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        mapp = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }
        res = []
        def backtrack(index, curr):
            if index >= len(digits):
                res.append(curr)
                return
            for i in mapp[digits[index]]:
                backtrack(index + 1, curr + i)
            return
        backtrack(0, "")
        return res


# ITERATIVE APPROACH
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        mapp = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }
        res = [""]
        for i in digits:
            new = []
            for j in res:
                for k in mapp[i]:
                    new.append(j + k)
            res = new
        return res
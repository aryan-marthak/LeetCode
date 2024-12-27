# 383. Ransom Note

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i not in magazine:
                return False
            for j in magazine:
                if i == j:
                    magazine = magazine.replace(j, "", 1)
                    break
        return True
    
# counter approach, slower but easier logic

count = Counter(magazine)

        for i in ransomNote:
            if count[i] == 0:
                return False
            else:
                count[i] -= 1
        return True
from collections import Counter

"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransom_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)

        for char , count in ransom_counter.items():
            if magazine_counter[char] < count:
                return False
        return True


if __name__ == "__main__":
    ransomNote = "aa"
    magazine = "ab"
    obj = Solution()
    print(obj.canConstruct(ransomNote, magazine))
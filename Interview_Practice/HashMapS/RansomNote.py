from collections import Counter

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
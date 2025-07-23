"""
Meta class
"""

class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        # Add a new attribute automatically
        dct['class_id'] = 123
        return super().__new__(cls, name, bases, dct)


class Solution(metaclass=MyMeta):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pattern_map = {}
        if len(pattern) != len(s.split()):
            return False
        for i in range(len(pattern)):
            if pattern[i] in pattern_map:
                if pattern_map[pattern[i]] != s.split()[i]:
                    return False
            pattern_map[pattern[i]] = s.split()[i]
        return True
    
    def wordPatternOptimal(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(pattern) != len(s.split()):
            return False
        p_s = {}
        s_p = {}
        for p, word in zip(pattern, words):
            if p in p_s:
                if p_s[p] != word:
                    return False
            p_s[p] = word

            if word in s_p:
                if s_p[word] != p:
                    return False
            s_p[word] = p

        return True


if __name__ == "__main__":
    pattern = "abba"
    s = "dog cat cat dog"
    obj = Solution()
    print(obj.wordPattern(pattern,s))
    pattern2 = "abba"
    s2 = "dog dog dog dog"
    print(obj.wordPatternOptimal(pattern2,s2))
    print(f"Class id = {obj.class_id}")


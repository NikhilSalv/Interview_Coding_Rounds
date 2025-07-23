"""
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern
and a non-empty word in s. Specifically:
Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.

"""

class Solution(object):
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
    
    def new_wordPatternOptimal(self, pattern, s):
        print("This is the monkey patched method!")
        return True


if __name__ == "__main__":
    pattern = "abba"
    s = "dog cat cat dog"
    obj = Solution()
    print(obj.wordPattern(pattern,s))
    pattern2 = "abba"
    s2 = "dog dog dog dog"

    obj.wordPatternOptimal = obj.new_wordPatternOptimal
    print(obj.wordPatternOptimal(pattern2,s2))


"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving 
the order of characters. No two characters may map to the same character, but a character may map to itself.
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t) or len(s) < 1:
            return False

        s_t = {}
        t_s = {}


        for i in range(len(s)):
            ch_s = s[i]
            ch_t = t[i]
            if ch_s in s_t:
                if s_t[ch_s] != ch_t:
                    return False
            else:
                s_t[ch_s] = ch_t
            
            if ch_t in t_s:
                if t_s[ch_t] != ch_s:
                    return False
            else:
                t_s[ch_t] = ch_s

        return True
    

if __name__ == "__main__":
    s = "egg"
    t = "add"
    obj = Solution()
    print(obj.isIsomorphic(s,t))
    print("Result:", obj.isIsomorphic(s, t))
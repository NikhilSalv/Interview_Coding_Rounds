"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some 
(can be none) of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).


"""

def isSubsequece(s,t):
    sunstring = []
    t_index = 0

    for i in range(len(s)):
        while t_index < len(t):
            if s[i] == t[t_index]:
                sunstring.append(s[i])
                t_index += 1
                break
            t_index += 1
    if s == "".join(sunstring):
        return True
    else:
        return False


if __name__ == "__main__":
    s = "abca"
    t = "ahbgdc"
    print(isSubsequece(s,t))
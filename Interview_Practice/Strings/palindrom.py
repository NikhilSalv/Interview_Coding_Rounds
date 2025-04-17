import re


def longest_palindromic_substring(s):
    if not s:
        return ""
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]  # Extract valid palindrome

    longest = ""
    for i in range(len(s)):
        # Odd-length palindrome 
        odd_palindrome = expand_around_center(i, i)
        # Even-length palindrome
        even_palindrome = expand_around_center(i, i + 1)

        # Update longest palindrome found
        longest = max(longest, odd_palindrome, even_palindrome, key=len)

    return longest

if __name__ == "__main__":
    string = "reverse this string and print"

    print(longest_palindromic_substring("babad"))  # Output: "bab" or "aba"
    print(longest_palindromic_substring("cbbd"))   # Output: "bb"
    print(longest_palindromic_substring("a"))      # Output: "a"
    print(longest_palindromic_substring("racecar")) # Output: "racecar"

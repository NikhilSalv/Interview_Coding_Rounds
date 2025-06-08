""""
Given a string s, find the length of the longest substring without duplicate characters.

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        visited = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            temp = s[right]
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[right])
            max_length = max(max_length, right - left +1)
        return max_length
    
    def lengthOfLongestSubstring2(self, s):
        visited = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in visited:
                visited.remove(s[left])  # ✅ Fix: remove s[left], not s[right]
                left += 1
            visited.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length
    
# Example usage
if __name__ == "__main__":
    s = "abcabcbbxyzwr"
    obj = Solution()
    print(obj.lengthOfLongestSubstring(s))  # Output: 3 (The answer is "abc", with the length of 3)
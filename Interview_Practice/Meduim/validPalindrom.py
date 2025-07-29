class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str


        b a b a d

        left= 0
        right = len(s)
        while left < right:
            if s[left] == s[right]:
                left_start = min(left_start, left)
                right_start = max(right_start, right)
                left +=1
                right -= 1
            else:
                left += 1
            if left
        """
        def expand(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right -1
        
        start, end = 0 ,0
        for i in range(len(s)-1):
            left1, right1 = expand(i,i)
            left2, right2 = expand(i,i+1)
            if right1 - left1 > end - start:
                start = left1
                end = right1
            if right2 - left2 > end - start:
                start = left2
                end = right2
        return s[start:end+1]
    

if __name__ == "__main__":
    s = "babad"
    x = 1432
    print(x//100)

    print()
    print(Solution().longestPalindrome(s))  # Output: "bab" or "aba"
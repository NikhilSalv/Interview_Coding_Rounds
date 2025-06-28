class Solution(object):
    def isPalindrome(self, s):
        normalised_string = "".join(char.lower() for char in s if char.isalnum())
        print(normalised_string)
        return normalised_string[::-1] == normalised_string
    

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    s1 = "0p"
    obj = Solution()

    print(obj.isPalindrome(s1))
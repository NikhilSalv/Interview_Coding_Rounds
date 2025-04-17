import re


def valid_palindrome(s):
    if not s:
        return True
    
    s = re.sub(r'[^a-zA-Z0-9]', "",s).lower()
    print(s)
    left , right = 0 , len(s) -1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    string = "A man, a plan, a fanal: vanama"
    result = valid_palindrome(string)
    print(result)
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

def validParenthesis(s):
    mapping = {")":"(","}":"{","]":"["}
    stack = []
    if len(s) < 2:
        return False
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            return False
    if stack:
        return False
    return True


if __name__ == "__main__":
    s= "()[(})]"
    s1 = "(]"
    s2 = "(({[]})"
    print(validParenthesis(s2))
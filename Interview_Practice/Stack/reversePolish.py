"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        def add(a,b):
            return int(a) + int(b)
        def sub(a,b):
            return int(a) - int(b)
        def multiply(a,b):
            return int(a) * int(b)
        def div(a,b):
            return int(float(a) / int(b))
        # mapping = {"":add,"":sub,"":,"":}
        for i in tokens:
            if i == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(add(first,second))
            elif i == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(sub(second,first))
            elif i == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(multiply(first,second))
            elif i == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(div(second,first))
            else:
                stack.append(i)
        return int(stack.pop())
            

        


if __name__ == "__main__":
    tokens = ["2","1","+","3","*"]
    tokens2 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    obj = Solution()
    print(obj.evalRPN(tokens2))
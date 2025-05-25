"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

"""

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
        

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_stack:
            return self.min_stack[-1]

if __name__ == "__main__":
    commands = ["MinStack","push","push","push","getMin","pop","top","getMin"]
    data = [[],[-2],[0],[-3],[],[],[],[]]
    output = [None] * len(commands)
    for i in range(len(commands)):
        if commands[i] == "MinStack":
            obj = MinStack()
        if commands[i] == "push":
            obj.push(data[i])
        if commands[i] == "getMin":
            pass
        if commands[i] == "pop":
            pass
        if commands[i] == "top":
            pass
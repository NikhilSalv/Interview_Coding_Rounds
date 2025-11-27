class MyStack(object):

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.pop(0))
        self.q1 , self.q2 = self.q2 , self.q1
        

    def pop(self):
        """
        :rtype: int
        """
        return self.q1.pop(0)
        

    def top(self):
        """
        :rtype: int
        """
        return self.q1[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.q1
    

if __name__ == "__main__":
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print(stack.top())   # returns 2
    print(stack.pop())   # returns 2
    print(stack.empty()) # returns False
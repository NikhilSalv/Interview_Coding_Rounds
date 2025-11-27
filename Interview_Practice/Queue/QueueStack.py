class MyQueue(object):

    def __init__(self):
        self.stack_in = []
        self.stack_out = []        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        self._move()
        return self.stack_out.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        self._move()
        return self.stack_out[-1]        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack_out and not self.stack_in


    def _move(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

if __name__ == "__main__":
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(queue.peek())  # returns 1
    print(queue.pop())   # returns 1
    print(queue.empty()) # returns False
class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k = k
        self.q = [0] * self.k
        self.front = -1
        self.rear = -1
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.k

        self.q[self.rear] = value
        return True


    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front +1 ) % self.k

        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.q[self.front]
        

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.q[self.rear]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.front == -1:
            return True
        return False
        

    def isFull(self):
        """
        :rtype: bool
        """
        return (self.rear + 1) % self.k == self.front
            
        

if __name__ == "__main__":
    circularQueue = MyCircularQueue(3)
    print(circularQueue.enQueue(1))  # return True
    print(circularQueue.enQueue(2))  # return True
    print(circularQueue.enQueue(3))  # return True
    print(circularQueue.enQueue(4))  # return False
    print(circularQueue.Rear())       # return 3
    print(circularQueue.isFull())     # return True
    print(circularQueue.deQueue())    # return True
    print(circularQueue.enQueue(4))  # return True
    print(circularQueue.Rear())       # return 4
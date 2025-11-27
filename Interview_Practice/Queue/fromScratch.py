class Queue:

	def __init__(self):

			self.q = []

			self.front = -1

			self.rear = -1

	def enqueue(self, value):

			if self.front == -1:

				self.front = 0

				self.rear = 0

			else:

				self.rear += 1

			self.q.append(value)

	def dequeue(self):

			if self.is_empty():

				return None

			value = self.q[self.front]



			self.front += 1



			if self.front > self.rear :

				self.front = -1

				self.rear = -1

				self.q = []

			return value



	def is_empty(self):

			return self.front ==  -1



	def get_first_element(self):

			if self.is_empty():

					return None



			return self.q[self.front]
	

if __name__ == "__main__":
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)
        print(queue.dequeue())  # Output: 10
        print(queue.get_first_element())  # Output: 20
        print(queue.is_empty())  # Output: False
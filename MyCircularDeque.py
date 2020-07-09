# https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque(object):
	def __init__(self, k):
		self.nitems = 0
		self.deque = [-1 for _ in range(k)]
		self.front = -1 
		self.rear = -1

	def insertFront(self, value):
		if self.isFull():
			return False

		if self.front == -1:
			if self.rear == -1:
				self.front = 1
				self.rear = 0
			else:
				self.front = self.rear

		self.front -= 1
		self.front %= len(self.deque)
		self.deque[self.front] = value
		self.nitems += 1

		return True

	def insertLast(self, value):
		if self.isFull():
			return False

		if self.rear == -1:
			if self.front == -1:
				self.rear = -1
				self.front = 0
			else:
				self.rear = self.front

		self.rear += 1
		self.rear %= len(self.deque)
		self.deque[self.rear] = value
		self.nitems += 1

		return True
	
	def deleteFront(self):
		if self.front == -1 or self.deque[self.front] == -1:
			return False

		self.deque[self.front] = -1
		self.front += 1
		self.front %= len(self.deque)
		self.nitems -= 1
        
		return True

	def deleteLast(self):
		if self.rear == -1 or self.deque[self.rear] == -1:
			return False

		self.deque[self.rear] = -1
		self.rear -= 1
		self.rear %= len(self.deque)
		self.nitems -= 1
        
		return True

	def getFront(self):
		return self.deque[self.front]

	def getRear(self):
		return self.deque[self.rear]

	def isEmpty(self):
		return self.nitems == 0
	
	def isFull(self):
		return self.nitems == len(self.deque)

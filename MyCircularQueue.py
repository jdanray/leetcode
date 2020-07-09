# https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue(object):
	def __init__(self, k):
		self.queue = [-1 for _ in range(k)]
		self.front = 0
		self.rear = -1

	def enQueue(self, value):
		if self.isFull():
			return False

		self.rear += 1
		self.rear %= len(self.queue)
		self.queue[self.rear] = value
		return True

	def deQueue(self):
		if self.isEmpty():
			return False
			
		self.queue[self.front] = -1
		self.front += 1
		self.front %= len(self.queue)
		return True

	def Front(self):
		return self.queue[self.front]   

	def Rear(self):
		return -1 if self.rear == -1 else self.queue[self.rear]

	def isEmpty(self):
		return self.Front() == self.Rear() == -1

	def isFull(self):
		return self.front != -1 and self.queue[self.front] != -1 and self.queue[(self.front + 1) % len(self.queue)] != -1 and self.queue[(self.front - 1) % len(self.queue)] != -1

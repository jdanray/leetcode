# https://leetcode.com/problems/implement-stack-using-queues/ 

class MyStack(object):
	def __init__(self):
		self.A = collections.deque()
		self.B = collections.deque()

	def push(self, x):
		if self.A:
			self.A.append(x)
		elif self.B:
			self.B.append(x)
		else:
			self.A.append(x)

	def pop(self):
		if self.A:
			while len(self.A) > 1:
				a = self.A.popleft()
				self.B.append(a)
			return self.A.popleft()
		elif self.B:
			while len(self.B) > 1:
				b = self.B.popleft()
				self.A.append(b)
			return self.B.popleft()

	def top(self):
		if self.A:
			while self.A:
				a = self.A.popleft()
				self.B.append(a)
			return a
		elif self.B:
			while self.B:
				b = self.B.popleft()
				self.A.append(b)
			return b

	def empty(self):
		return not self.A and not self.B

# After I solve a problem, I like to study other people's solutions
# In this case, I found a MUCH simpler solution:
# https://leetcode.com/problems/implement-stack-using-queues/discuss/62519/Only-push-is-O(n)-others-are-O(1).-Using-one-queue.-Combination-of-two-shared-solutions
# Here is my Python implementation:

class MyStack(object):
	def __init__(self):
		self.queue = collections.deque()

	def push(self, x):
		self.queue.append(x)
		for _ in range(len(self.queue) - 1):
			self.queue.append(self.queue.popleft())

	def pop(self):
		return self.queue.popleft()

	def top(self):
		return self.queue[0]

	def empty(self):
		return not self.queue

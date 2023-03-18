# https://leetcode.com/problems/design-browser-history/

class Node(object):
	def __init__(self, val, prev):
		self.val = val
		self.prev = prev
		self.next = None

class BrowserHistory(object):
	def __init__(self, homepage):
		self.cur = Node(homepage, None)

	def visit(self, url):
		cur = self.cur
		self.cur = Node(url, self.cur)
		cur.next = self.cur

	def back(self, steps):
		while steps > 0 and self.cur.prev != None:
			self.cur = self.cur.prev
			steps -= 1

		return self.cur.val

	def forward(self, steps):
		while steps > 0 and self.cur.next != None:
			self.cur = self.cur.next
			steps -= 1

		return self.cur.val

# Simpler solution: 

class BrowserHistory(object):
	def __init__(self, homepage):
		self.history = [homepage]
		self.loc = 0

	def visit(self, url):
		self.loc += 1
		self.history = self.history[:self.loc]
		self.history.append(url)

	def back(self, steps):
		self.loc = max(0, self.loc - steps)
		return self.history[self.loc]

	def forward(self, steps):
		self.loc = min(len(self.history) - 1, self.loc + steps)
		return self.history[self.loc]

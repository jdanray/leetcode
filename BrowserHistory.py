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

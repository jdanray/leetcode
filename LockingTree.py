# https://leetcode.com/problems/operations-on-tree/ 

class LockingTree(object):
	def __init__(self, parent):
		self.locked = collections.defaultdict(str)
		self.parent = parent

		self.children = collections.defaultdict(list)
		for u in range(len(self.parent)):
			self.children[self.parent[u]].append(u)

	def lock(self, num, user):
		if not self.locked[num]:
			self.locked[num] = user
			return True
		else:
			return False

	def unlock(self, num, user):
		if self.locked[num] == user:
			self.locked[num] = ''
			return True
		else:
			return False

	def upgrade(self, num, user):
		u = num
		while u != -1:
			if self.locked[u]:
				return False
			u = self.parent[u]

		unlocked = False
		stack = [u for u in self.children[num]]
		while stack:
			u = stack.pop()

			if self.locked[u]:
				unlocked = True
				self.locked[u] = ''

			for v in self.children[u]:
				stack.append(v)

		if unlocked:
			self.locked[num] = user
			return True
		else:
			return False

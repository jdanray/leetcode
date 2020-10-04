# https://leetcode.com/problems/throne-inheritance/ 

class ThroneInheritance(object):
	def __init__(self, kingName):
		self.dead = set()
		self.tree = {kingName: []}
		self.root = kingName

	def birth(self, parentName, childName):
		self.tree[parentName].append(childName)
		self.tree[childName] = []

	def death(self, name):
		self.dead.add(name)

	def getInheritanceOrder(self):
		def dfs(root):
			res = []
			if root not in self.dead:
				 res += [root]

			for child in self.tree[root]:
				res += dfs(child)
			return res

		return dfs(self.root)

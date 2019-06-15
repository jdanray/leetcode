# https://leetcode.com/problems/map-sum-pairs/

class TrieNode(object):
	def __init__(self):
		self.edges = dict()
		self.leaf = False
		
class MapSum(object):
	def __init__(self):
		self.root = TrieNode()
	
	def insert(self, key, val):
		curr = self.root
		for letter in key:
			if letter not in curr.edges:
				curr.edges[letter] = TrieNode()
			curr = curr.edges[letter]
		curr.leaf = val

	def sum(self, prefix):
		curr = self.root
		for letter in prefix:
			if letter not in curr.edges:
				return 0
			curr = curr.edges[letter]

		s = 0
		stack = [curr]
		while stack:
			node = stack.pop()

			if node.leaf != False:
				s += node.leaf

			for v in node.edges.values():
				stack.append(v)

		return s

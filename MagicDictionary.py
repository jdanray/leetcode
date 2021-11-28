# https://leetcode.com/problems/implement-magic-dictionary/

class DictNode(object):
	def __init__(self):
		self.edges = dict()
		self.leaf = False

class MagicDictionary(object):
	def __init__(self):
		self.root = DictNode()

	def buildDict(self, dictionary):
		for word in dictionary:
			self.insert(word)

	def insert(self, word):
		cur = self.root
		for letter in word:
			if letter not in cur.edges:
				cur.edges[letter] = DictNode()
			cur = cur.edges[letter]
		cur.leaf = True

	def search(self, searchWord):
		def do_search(cur, i, missed):
			if i >= len(searchWord):
				return cur.leaf and missed

			if not missed:
				return any(do_search(cur.edges[letter], i + 1, letter != searchWord[i]) for letter in cur.edges)

			if searchWord[i] not in cur.edges:
				return False

			return do_search(cur.edges[searchWord[i]], i + 1, True)

		return do_search(self.root, 0, False)

# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class DictNode(object):
	def __init__(self):
		self.edges = dict()
		self.leaf = False
		
class WordDictionary(object):
	def __init__(self):
		self.root = DictNode()
	
	def addWord(self, word):
		cur = self.root
		for letter in word:
			if letter not in cur.edges:
				cur.edges[letter] = DictNode()
			cur = cur.edges[letter]
		cur.leaf = True

	def search(self, word):
		def do_search(cur, i):
			if i >= len(word):
				return cur.leaf

			if word[i] == '.':
				return any(do_search(cur.edges[letter], i + 1) for letter in cur.edges)

			if word[i] not in cur.edges:
				return False

			return do_search(cur.edges[word[i]], i + 1)

		return do_search(self.root, 0)

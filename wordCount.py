# https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/

class TrieNode(object):
	def __init__(self):
		self.edges = dict()
		self.leaf = False
		
class Trie:
	def __init__(self):
		self.root = TrieNode()
	
	def insert(self, word):
		curr = self.root
		for letter in word:
			if letter not in curr.edges:
				curr.edges[letter] = TrieNode()
			curr = curr.edges[letter]
		curr.leaf = True

	def search(self, word):
		curr = self.root
		for letter in word:
			if letter not in curr.edges:
				return False
			curr = curr.edges[letter]
		return curr.leaf

class Solution(object):
	def wordCount(self, startWords, targetWords):
		trie = Trie()
		for s in startWords:
			trie.insert(sorted(s))

		res = 0
		for t in targetWords:
			t = sorted(t)
			if any(trie.search(t[:i] + t[i + 1:]) for i in range(len(t))):
				res += 1

		return res

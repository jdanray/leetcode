# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

class TrieNode(object):
	def __init__(self):
		self.edges = dict()
		self.n = 0 
		
class Trie:
	def __init__(self):
		self.root = TrieNode()
	
	def insert(self, word):
		curr = self.root
		for letter in word:
			if letter not in curr.edges:
				curr.edges[letter] = TrieNode()
			curr = curr.edges[letter]
			curr.n += 1

	def search(self, word):
		res = 0
		curr = self.root
		for letter in word:
			curr = curr.edges[letter]
			res += curr.n
		return res

class Solution(object):
	def sumPrefixScores(self, words):
		trie = Trie()

		for w in words:
			trie.insert(w)

		return [trie.search(w) for w in words]

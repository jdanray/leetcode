# https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode(object):
	def __init__(self):
		self.nodes = dict()
		self.leaf = False
		
class Trie(object):
	def __init__(self):
		self.root = TrieNode()
	
	def insert(self, word):
		curr = self.root
		for letter in word:
			if letter not in curr.nodes:
				curr.nodes[letter] = TrieNode()
			curr = curr.nodes[letter]
			
		curr.leaf = True

	def search(self, word):
		curr = self.root
		for letter in word:
			if letter in curr.nodes:
				curr = curr.nodes[letter]
			else:
				return False
				
		return curr.leaf

	def startsWith(self, prefix):
		curr = self.root
		for letter in prefix:
			if letter in curr.nodes:
				curr = curr.nodes[letter]
			else:
				return False
				
		return True

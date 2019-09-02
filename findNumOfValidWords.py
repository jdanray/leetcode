# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

class TrieNode(object):
	def __init__(self):
		self.edges = dict()
		self.count = 0
		
class Trie:
	def __init__(self):
		self.root = TrieNode()
	
	def insert(self, word):
		curr = self.root
		for letter in word:
			if letter not in curr.edges:
				curr.edges[letter] = TrieNode()
			curr = curr.edges[letter]
		curr.count += 1

class Solution(object):
	def findNumOfValidWords(self, words, puzzles):
		trie = Trie()
		for w in words:
			trie.insert(sorted(set(w)))

		res = [0 for _ in range(len(puzzles))]
		for i, p in enumerate(puzzles):
			first = p[0]
			puzzle = sorted(p)
			stack = [[trie.root, False]]
			while stack:
				node, firstLetter = stack.pop()

				if firstLetter:
					res[i] += node.count

				for letter in puzzle:
					if letter in node.edges:
						if letter == first:
							stack.append([node.edges[letter], True])
						else:
							stack.append([node.edges[letter], firstLetter])
		return res

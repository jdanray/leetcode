# https://leetcode.com/problems/keyboard-row/description/

class Solution:
	row = {'q': 0, 'w': 0, 'e': 0, 'r': 0, 't': 0, 'y': 0, 'u': 0, 'i': 0, 'o': 0, 'p': 0, 'a': 1, 's': 1, 'd': 1, 'f': 1, 'g': 1, 'h': 1, 'j': 1, 'k': 1, 'l': 1, 'z': 2, 'x': 2, 'c': 2, 'v': 2, 'b': 2, 'n': 2, 'm': 2}
	def findWords(self, words):
		ret = []
		for w in words:
			r = set()
			for c in w:
				r.add(self.row[c.lower()])
			if len(r) == 1:
				ret.append(w)
		return ret

class Solution(object):
	def findWords(self, words):
		rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
		return [w for w in words for r in rows if all(c.lower() in r for c in w)]

class Solution:
	def findWords(self, words):
		keyrows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
		onerows = []
		for wrd in words:
			for r in keyrows:
				w = ''.join(c.lower() for c in wrd)
				if all(c in r for c in w):
					onerows.append(wrd)
		return onerows

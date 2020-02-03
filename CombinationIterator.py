# https://leetcode.com/problems/iterator-for-combination/

class CombinationIterator(object):
	def allCombos(self, chars, start, length, res):
		if length == 0:
			self.combos.append(res)
			return

		for i in range(start, len(chars) - length + 1):
			self.allCombos(chars, i + 1, length - 1, res + chars[i])

	def __init__(self, characters, combinationLength):
		self.combos = []
		self.allCombos(characters, 0, combinationLength, "")

	def next(self):
		return self.combos.pop(0)

	def hasNext(self):
		return not not self.combos

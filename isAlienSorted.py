# https://leetcode.com/contest/weekly-contest-114/problems/verifying-an-alien-dictionary/

class Solution(object):
	def isAlienSorted(self, words, order):
		index = {c: i for i, c in enumerate(order)}
		for i in range(len(words) - 1):
			j = 0
			while j < len(words[i]) and j < len(words[i + 1]) and words[i][j] == words[i + 1][j]:
				j += 1

			if j < len(words[i]) and (j >= len(words[i + 1]) or index[words[i][j]] > index[words[i + 1][j]]):
				return False

		return True

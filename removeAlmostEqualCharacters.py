# https://leetcode.com/problems/remove-adjacent-almost-equal-characters/ 

class Solution(object):
	def removeAlmostEqualCharacters(self, word):
		N = len(word)
		loc = {c: i for i, c in enumerate(string.ascii_lowercase)}
		isAlmostEqual = lambda a, b: abs(loc[a] - loc[b]) in [0, 1]

		i = 0
		res = 0
		while i < N - 1:
			l = 1
			while i < N - 1 and isAlmostEqual(word[i], word[i + 1]):
				i += 1
				l += 1

			res += l // 2
			i += 1

		return res

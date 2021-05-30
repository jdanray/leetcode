# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

class Solution(object):
	def isSumEqual(self, firstWord, secondWord, targetWord):
		val = {c: i for i, c in enumerate(string.ascii_lowercase)}
		def numVal(word):
			res = 0
			"""
			place = 1
			for c in word[::-1]:
				res += val[c] * place
				place *= 10
			"""
			for c in word:
				res *= 10
				res += val[c]
			return res

		return numVal(firstWord) + numVal(secondWord) == numVal(targetWord)

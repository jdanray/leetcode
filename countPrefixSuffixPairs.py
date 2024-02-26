# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/ 

class Solution(object):
	def countPrefixSuffixPairs(self, words):
		def isPrefixAndSuffix(a, b):
			return b[:len(a)] == a and b[-len(a):] == a

		res = 0
		for j in range(len(words)):
			for i in range(j):
				if isPrefixAndSuffix(words[i], words[j]):
					res += 1

		return res

# https://leetcode.com/problems/merge-strings-alternately/ 

class Solution(object):
	def mergeAlternately(self, word1, word2):
		M = len(word1)
		N = len(word2)
		i = 0
		j = 0
		res = ""
		while i < M or j < N:
			if i < M and j < N:
				res += word1[i]
				res += word2[j]
				i += 1
				j += 1
			elif i < M:
				res += word1[i]
				i += 1
			else:
				res += word2[j]
				j += 1
		return res

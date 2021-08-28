# https://leetcode.com/problems/largest-merge-of-two-strings/ 

class Solution(object):
	def largestMerge(self, word1, word2):
		M = len(word1)
		N = len(word2)

		i = 0
		j = 0
		res = ''
		while i < M or j < N:
			k = i
			l = j
			while k < M and l < N and word1[k] == word2[l]:
				k += 1
				l += 1

			if k < M and l < N:
				if word1[k] > word2[l]:
					res += word1[i]
					i += 1
				else:
					res += word2[j]
					j += 1
			elif k < M:
				res += word1[i]
				i += 1
			else:
				res += word2[j]
				j += 1

		return res

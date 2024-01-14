# https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/ 

class Solution(object):
	def beautifulIndices(self, s, a, b, k):
		N = len(s)

		def indexes(p):
			j = 0
			res = []
			for i in range(N):
				j = 0
				while i + j < N and j < len(p) and s[i + j] == p[j]:
					j += 1

				if j == len(p):
					res.append(i)

			return res 

		aIdxs = indexes(a)
		bIdxs = indexes(b)

		l = 0
		res = []
		for i in aIdxs:
			while l < len(bIdxs) and bIdxs[l] < i - k:
				l += 1

			if l < len(bIdxs) and bIdxs[l] <= i + k:
				res.append(i) 

		return res 

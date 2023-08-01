# https://leetcode.com/problems/combinations/

class Solution(object):
	def combine(self, n, k):
		if k == 0:
			return [[]]

		res = []
		for j in range(1, n + 1):
			for c in self.combine(j - 1, k - 1):
				res.append(c + [j])
		return res

class Solution:
	def combine(self, n, k):
		if k == 0:
			return [[]]
		
		prev = self.combine(n, k - 1)
		res = []
		for p in prev:
			s = p[-1] if p else 0
			for i in range(s + 1, n + 1):
				res.append(p + [i])
		return res

class Solution:
	def combine(self, n, k):
		prev = [[]]
		for _ in range(k):
			res = []
			for p in prev:
				s = p[-1] if p else 0
				for i in range(s + 1, n + 1):
					res.append(p + [i])
			prev = res
		return prev

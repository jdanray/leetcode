# https://leetcode.com/problems/calculate-digit-sum-of-a-string/

class Solution(object):
	def digitSum(self, s, k):
		if len(s) <= k:
			return s

		groups = []
		for i in range(0, len(s), k):
			groups.append([])
			for j in range(i, min(len(s), i + k)):
				groups[-1].append(s[j])

		res = ''
		for g in groups:
			n = 0
			for d in g:
				n += int(d)
			res += str(n)

		return self.digitSum(res, k)

class Solution(object):
	def digitSum(self, s, k):
		if len(s) <= k:
			return s

		groups = [s[i:i+k] for i in range(0, len(s), k)]
		res = ''.join(str(sum(int(d) for d in g)) for g in groups)
		return self.digitSum(res, k)

class Solution(object):
	def digitSum(self, s, k):
		return s if len(s) <= k else self.digitSum(''.join(str(sum(int(d) for d in g)) for g in [s[i:i+k] for i in range(0, len(s), k)]), k)

class Solution(object):
	def digitSum(self, s, k):
		while len(s) > k:
			s = ''.join(str(sum(int(d) for d in g)) for g in [s[i:i+k] for i in range(0, len(s), k)])
		return s

# https://leetcode.com/problems/find-the-least-frequent-digit/

class Solution(object):
	def getLeastFrequentDigit(self, n):
		count = collections.Counter()
		while n > 0:
			count[n % 10] += 1
			n //= 10

		res = [-1, float('inf')]
		for d in count:
			if count[d] < res[1] or (count[d] == res[1] and d < res[0]):
				res = [d, count[d]]

		return res[0]
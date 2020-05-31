# https://leetcode.com/problems/count-largest-group/ 

class Solution(object):
	def countLargestGroup(self, n):
		def digitsum(num):
			s = 0
			while num > 0:
				s += (num % 10)
				num //= 10
			return s

		count = collections.Counter(digitsum(k) for k in range(1, n + 1))
		m = max(count.values())
		return len(k for k in count if count[k] == m)

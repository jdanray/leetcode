# https://leetcode.com/problems/find-the-pivot-integer/ 

class Solution(object):
	def pivotInteger(self, n):
		tot = n * (n + 1) // 2
		s = 0
		for u in range(1, n + 1):
			s += u
            
			if s == tot:
				return u
            
			tot -= u

		return -1

class Solution(object):
	def pivotInteger(self, n):
		pre = collections.defaultdict(int)
		s = 0
		for i in range(1, n + 1):
			s += i
			pre[i] = s

		s = 0
		for i in range(n, 0, -1):
			s += i
			if pre[i] == s:
				return i

		return -1

# https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/ 

class Solution(object):
	def queryString(self, S, N):
		nums = set()
		for i in range(len(S) - 1, -1, -1):
			n = 0
			p = 1
			for j in range(i, -1, -1):
				n += int(S[j]) * p
				p <<= 1
				nums.add(n)

		n = 1
		while n <= N:
			if n not in nums:
				return False
			n += 1

		return True

class Solution(object):
	def queryString(self, S, N):
		seen = set()
		rest = N
		i = len(S) - 1
		while i >= 0 and rest > 0:
			n = 0
			p = 1
			j = i
			while j >= 0 and n <= N:
				n += int(S[j]) * p
				p <<= 1
				if n > 0 and n <= N and n not in seen:
					rest -= 1
					seen.add(n)
				j -= 1
			i -= 1

		return rest == 0

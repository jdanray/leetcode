# https://leetcode.com/problems/can-convert-string-in-k-moves/ 

class Solution(object):
	def canConvertString(self, s, t, k):
		if len(t) != len(s):
			return False
        
		N = 26
		avail = [k // N for _ in range(N + 1)]
		for x in range(1, k % N + 1):
			avail[x] += 1

		for i in range(len(s)):
			if s[i] == t[i]:
				continue

			if t[i] > s[i]:
				shift = ord(t[i]) - ord(s[i])
			else:
				shift = (ord('z') - ord(s[i])) + (ord(t[i]) - ord('a')) + 1

			avail[shift] -= 1
			if avail[shift] < 0:
				return False

		return True

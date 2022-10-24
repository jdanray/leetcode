# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/ 

class Solution(object):
	def maxLength(self, arr):
		N = len(arr)
		char2bit = {c: b for b, c in enumerate(string.ascii_lowercase)}

		def solve(i, used):
			if i >= N:
				l = 0
				while used > 0:
					if used & 1:
						l += 1
					used >>= 1
				return l

			excl = solve(i + 1, used)

			for c in arr[i]:
				b = char2bit[c]
				if (used >> b) & 1:
					return excl
				else:
					used ^= (1 << b)

			incl = solve(i + 1, used) 
	
			return max(excl, incl)

		return solve(0, 0)

# https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/ 

class Solution(object):
	fives = {'1', '101', '11001', '1111101', '1001110001', '110000110101', '11110100001001'}

	def minimumBeautifulSubstrings(self, s):
		def backtrack(i, sub):
			if i >= len(s):
				if not sub or sub in self.fives:
					return 1
				else:
					return float('inf')

			sub += s[i]
			part = backtrack(i + 1, sub)
			if sub in self.fives:
				return min(part, 1 + backtrack(i + 1, ''))
			else:
				return part

		res = backtrack(0, '')
		return -1 if res == float('inf') else res

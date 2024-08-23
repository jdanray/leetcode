# https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/ 

# Sliding window
# O(N)
class Solution(object):
	def countKConstraintSubstrings(self, s, k):
		ones = 0
		zeros = 0
		i = 0
		res = 0
		for j, c in enumerate(s):
			if c == '1':
				ones += 1
			else:
				zeros += 1

			while ones > k and zeros > k:
				if s[i] == '1':
					ones -= 1
				else:
					zeros -= 1
				i += 1

			res += j - i + 1

		return res

# O(N**2)
class Solution(object):
	def countKConstraintSubstrings(self, s, k):
		res = 0
		for i in range(len(s)):
			j = i
			ones = 0
			zeros = 0
			while j >= 0 and (ones <= k or zeros <= k):
				if s[j] == '1':
					ones += 1
				else:
					zeros += 1

				if ones <= k or zeros <= k:
					res += 1

				j -= 1

		return res

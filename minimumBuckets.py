# https://leetcode.com/problems/minimum-number-of-buckets-required-to-collect-rainwater-from-houses/ 

class Solution(object):
	def minimumBuckets(self, street):
		N = len(street)

		covered = -1
		res = 0
		for i, s in enumerate(street):
			if s == '.' or i == covered:
				continue

			if i + 1 < N and street[i + 1] == '.':
				res += 1
				if i + 2 < N and street[i + 2] == 'H':
					covered = i + 2
			elif i - 1 >= 0 and street[i - 1] == '.':
				res += 1
			else:
				return -1

		return res

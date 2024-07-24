# https://leetcode.com/problems/sort-the-jumbled-numbers/ 

class Solution(object):
	def sortJumbled(self, mapping, nums):
		vals = []
		for i, n in enumerate(nums):
			if n == 0:
				vals.append((mapping[0], i))
				continue

			p = 0
			m = 0
			while n > 0:
				m += mapping[n % 10] * 10 ** p
				p += 1
				n //= 10

			vals.append((m, i))

		return [nums[i] for (_, i) in sorted(vals)]

class Solution(object):
	def sortJumbled(self, mapping, nums):
		def convert(num):
			if num == 0:
				return mapping[0]

			res = 0
			place = 1
			while num > 0:
				d = num % 10
				res += place * mapping[d]
				place *= 10
				num //= 10
			return res

		res = sorted((convert(n), i) for i, n in enumerate(nums))
		return [nums[r[1]] for r in res]

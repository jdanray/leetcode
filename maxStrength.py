# https://leetcode.com/problems/maximum-strength-of-a-group/

class Solution(object):
	def maxStrength(self, nums):
		def prod(nums): 
			return functools.reduce(lambda x, y: x * y, nums) if nums else 1

		pos = [n for n in nums if n > 0]
		neg = sorted([n for n in nums if n < 0])
		zero = any(n == 0 for n in nums)

		if not pos and not neg:
			return 0

		if len(neg) == 1:
			return prod(pos) if pos else 0 if zero else neg[0]
		elif len(neg) % 2 == 1:
			return prod(neg[:-1]) * prod(pos)
		else:
			return prod(neg) * prod(pos)


class Solution(object):
	def maxStrength(self, nums):
		def prod(nums): 
			return functools.reduce(lambda x, y: x * y, nums)

		pos = [n for n in nums if n > 0]
		neg = sorted([n for n in nums if n < 0])
		zero = any(n == 0 for n in nums)

		if not pos and not neg:
			return 0

		if not pos:
			if len(neg) == 1:
				return 0 if zero else neg[0]
			elif len(neg) % 2 == 1:
				return prod(neg[:-1])
			else:
				return prod(neg)

		if not neg:
			return prod(pos)

		if pos and neg:
			if len(neg) == 1:
				return prod(pos)
			elif len(neg) % 2 == 1:
				return prod(neg[:-1]) * prod(pos)
			else:
				return prod(neg) * prod(pos)

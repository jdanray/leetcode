# https://leetcode.com/problems/finding-3-digit-even-numbers/

class Solution(object):
	def findEvenNumbers(self, digits):
		res = set()
		for i, a in enumerate(digits):
			if a % 2 == 1: 
				continue

			for j, b in enumerate(digits):
				if j == i: 
					continue

				for k, c in enumerate(digits):
					if k == i or k == j or c == 0:
						continue

					res.add(100*c + 10*b + a)

		return sorted(res)

class Solution(object):
	def findEvenNumbers(self, digits):
		nums = set()
		def build(n):
			if len(n) == 3:
				r = digits[n[0]] + (digits[n[1]] * 10) + (digits[n[2]] * 100)
				nums.add(r)
				return True

			for i, d in enumerate(digits):
				if i not in n and (n or d % 2 == 0) and (len(n) != 2 or d != 0):
					build(n + [i])

		build([])
		return sorted(nums)

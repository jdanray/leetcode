# https://leetcode.com/problems/four-divisors/ 

class Solution(object):
	def sumFourDivisors(self, nums):
		D = 4

		res = 0
		for n in nums:
			divisors = set()
			for d in range(1, int(math.ceil(math.sqrt(n))) + 1):
				if n % d == 0:
					divisors.add(d)
					divisors.add(n // d)

			if len(divisors) == D:
				res += sum(divisors)

		return res

# https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/description/ 

class Solution(object):
	def sumDigitDifferences(self, nums):
		digits = [[0 for _ in range(10)] for _ in range(10)] # digits[p][d] is the count of digit d at the p-th position
		res = 0
		for n in nums:
			p = 0
			while n > 0:
				d = n % 10
				for j in range(len(digits[p])):
					if digits[p][j] > 0 and j != d:
						res += digits[p][j]

				digits[p][d] += 1
				p += 1
				n //= 10

		return res

"""
After I solve a problem, I like to study other people's solutions. I found a faster solution here: https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/discuss/5177096/Summation-of-freq*(total-freq)

I rewrote the C++ solution into Python:
"""

class Solution(object):
	def sumDigitDifferences(self, nums):
		digits = [[0 for _ in range(10)] for _ in range(10)] 
		for n in nums:
			i = 0
			while n > 0:
				digits[i][n % 10] += 1
				i += 1
				n //= 10

		res = 0
		for i in range(len(digits)):
			for j in range(len(digits[0])):
				res += digits[i][j] * (len(nums) - digits[i][j])

		return res // 2

# https://leetcode.com/problems/number-of-beautiful-pairs/ 

class Solution(object):
	def countBeautifulPairs(self, nums):
		N = len(nums)

		def firstDigit(num):
			res = 0
			while num > 0:
				res = num % 10
				num //= 10
			return res

		def lastDigit(num):
			return num % 10

		res = 0
		for i in range(N):
			for j in range(i + 1, N):
				f = firstDigit(nums[i])
				l = lastDigit(nums[j])

				if math.gcd(f, l) == 1:
					res += 1

		return res

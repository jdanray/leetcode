# https://leetcode.com/problems/prime-in-diagonal/ 

class Solution(object):
	def diagonalPrime(self, nums):
		N = len(nums)

		def isPrime(n):
			if n == 1:
				return False
            
			for d in range(2, int(math.sqrt(n)) + 2):
				if n % d == 0 and d != n:
					return False
                
			return True

		res = 0
		for i in range(N):
			if isPrime(nums[i][i]):
				res = max(res, nums[i][i])

			if isPrime(nums[i][N - i - 1]):
				res = max(res, nums[i][N - i - 1])

		return res

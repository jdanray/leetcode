# https://leetcode.com/problems/count-nice-pairs-in-an-array/ 

class Solution(object):
	def countNicePairs(self, nums):
		MOD = 10**9 + 7

		def rev(n):
			r = 0
			while n > 0:
				r *= 10
				r += (n % 10)
				n //= 10                
			return r

		seen = collections.Counter()
		res = 0
		for n in nums:
			s = n - rev(n)
            
			res += seen[s]
			res %= MOD
            
			seen[s] += 1

		return res

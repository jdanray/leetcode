# https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/ 

class Solution(object):
	def countDistinctIntegers(self, nums):
		nums = set(nums)
		rev = set()
		for n in nums:
			r = 0
			while n > 0:
				r *= 10
				r += (n % 10)
				n //= 10
                
			rev.add(r)

		return len(nums | rev)

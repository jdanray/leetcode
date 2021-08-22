# https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution(object):
	def findGCD(self, nums):
		def gcd(a, b):
			if a == 0:
				return b
			elif b == 0:
				return a
			elif a > b:
				return gcd(a - b, b)
			else:
				return gcd(a, b - a)

		return gcd(min(nums), max(nums))

class Solution(object):
	def findGCD(self, nums):
		a = min(nums)
		b = max(nums)
		while a > 0 and b > 0:
			if a > b:
				a, b = a - b, b
			else:
				a, b = a, b - a

		return a if b == 0 else b 

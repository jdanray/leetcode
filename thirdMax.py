# https://leetcode.com/problems/third-maximum-number/

# https://leetcode.com/problems/third-maximum-number/

class Solution(object):
	def thirdMax(self, nums):
		max1 = -sys.maxsize
		max2 = -sys.maxsize
		max3 = -sys.maxsize
		for n in nums:
			if n == max1 or n == max2 or n == max3:
				continue
			elif n > max1:
				max3 = max2
				max2 = max1
				max1 = n
			elif n > max2:
				max3 = max2
				max2 = n
			elif n > max3:
				max3 = n
                
		return max1 if max3 == -sys.maxsize else max3

class Solution(object):
	def thirdMax(self, nums):
		max1 = -sys.maxsize
		max2 = -sys.maxsize
		max3 = -sys.maxsize
		seen = set()       
		for n in nums:
			if n in seen:
				continue
			elif n > max1:
				max3 = max2
				max2 = max1
				max1 = n
			elif n > max2:
				max3 = max2
				max2 = n
			elif n > max3:
				max3 = n
                
			seen.add(n)
            
		return max1 if max3 == -sys.maxsize else max3

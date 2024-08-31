# https://leetcode.com/problems/count-almost-equal-pairs-i/ 

class Solution(object):
	def countPairs(self, nums):
		res = 0
		for j in range(len(nums)):
			for i in range(j):
				x = nums[i]
				y = nums[j]

				swap = True
				misses = 0
				xmiss = -1
				ymiss = -1

				while x > 0 or y > 0:
					bx = x % 10
					by = y % 10

					if bx != by:
						misses += 1
                        
						if misses == 1:
							xmiss = bx
							ymiss = by
						elif bx != ymiss or by != xmiss:
							swap = False
	
					x //= 10
					y //= 10

				if misses == 0 or (misses == 2 and swap): 
					res += 1

		return res

# https://leetcode.com/problems/smallest-value-of-the-rearranged-number/ 

class Solution(object):
	def smallestNumber(self, num):
		pos = (num > 0)
        
		num = abs(num)
		count = collections.Counter()
		while num > 0:
			d = num % 10
			count[d] += 1
			num //= 10

		res = 0
		for d in range(10):
			if pos and res == 0:
				res = min(d for d in count if d != 0)
				count[res] -= 1

			if not pos:
				d = 10 - d - 1			

			while count[d] > 0:
				res *= 10
				res += d
				count[d] -= 1

		return res if pos else -res

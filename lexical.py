# https://leetcode.com/problems/lexicographical-numbers/

class Solution:
	def lexicalOrder(self, n):
		result = []
		def order(num):
			if len(result) >= n:
				return True
			if num > 0:
				result.append(num)
			b = num * 10
			for c in range(10):
				newnum = b + c
				if newnum != 0 and newnum <= n:
					order(newnum)
		order(0)
		return result

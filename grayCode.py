# https://leetcode.com/problems/gray-code/

class Solution(object):
	def grayCode(self, n):
		if n == 0:
			return [0]

		res = self.grayCode(n - 1)
		for num in res[::-1]:
			res.append(num + (1 << (n - 1))) 
            
		return res

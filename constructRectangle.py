# https://leetcode.com/problems/construct-the-rectangle/ 

class Solution(object):
	def constructRectangle(self, area):
		res = [area, 1]
		for w in range(1, int(math.sqrt(area)) + 1):
			if area % w == 0:
				l = area // w
				if l - w < res[0] - res[1]:
					res = [l, w]
            
		return res

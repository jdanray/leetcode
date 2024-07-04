# https://leetcode.com/problems/maximum-height-of-a-triangle/ 

class Solution(object):
	def maxHeightOfTriangle(self, red, blue):
		def height(a, b):
			h = 1
			while a >= h:
				a -= h
				h += 1

				if b < h:
					break

				b -= h
				h += 1

			return h - 1

		return max(height(red, blue), height(blue, red))

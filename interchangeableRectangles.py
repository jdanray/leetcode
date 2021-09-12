# https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/ 

class Solution(object):
	def interchangeableRectangles(self, rectangles):
		count = collections.Counter()
		res = 0
		for (w, h) in rectangles:
			ratio = 1.0 * w / h

			if ratio in count:
				res += count[ratio]

			count[ratio] += 1

		return res

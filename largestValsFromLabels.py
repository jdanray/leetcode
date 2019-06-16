# https://leetcode.com/problems/largest-values-from-labels/

class Solution(object):
	def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
		count = collections.defaultdict(int)
		vabels = sorted(zip(values, labels), reverse=True)
		s = 0
		n = 0
		for v, l in vabels:
			if n >= num_wanted:
				break

			if count[l] < use_limit:
				s += v
				count[l] += 1
				n += 1

		return s

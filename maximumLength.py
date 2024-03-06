# https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/ 

class Solution(object):
	def maximumLength(self, nums):
		count = collections.Counter(nums)
		l = collections.defaultdict(int)
		res = 0
		for n in sorted(count.keys()):
			if n == 1:
				res = max(res, count[n] - (count[n] % 2 == 0))
			else:
				res = max(res, l[n] * 2 + 1)
				if count[n] >= 2:
					l[n ** 2] = l[n] + 1
                    
		return res

# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/ 

class Solution(object):
	def minimumRecolors(self, blocks, k):
		N = len(blocks)
		res = float('inf')
		for i in range(N - k + 1):
			w = 0
			for j in range(i, i + k):
				if blocks[j] == 'W':
					w += 1
			res = min(res, w)
		return res

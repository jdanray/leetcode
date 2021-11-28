# https://leetcode.com/problems/distant-barcodes/ 

class Solution(object):
	def rearrangeBarcodes(self, barcodes):
		N = len(barcodes)

		count = collections.Counter(barcodes)
		maxCode = max(count, key=lambda c: count[c])
		res = [0 for _ in range(N)]
		idx = 0
		while count[maxCode] > 0:
			res[idx] = maxCode
			idx += 2
			count[maxCode] -= 1

		for c in count:
			while count[c] > 0:
				if idx >= N:
					idx = 1

				res[idx] = c
				idx += 2
				count[c] -= 1

		return res

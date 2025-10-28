# https://leetcode.com/problems/make-array-elements-equal-to-zero/

class Solution(object):
	def countValidSelections(self, nums):
		N = len(nums)

		def isValid(cur, direct):
			lnums = [n for n in nums]
			nzeros = lnums.count(0)
			while nzeros < N and cur >= 0 and cur < N:
				if lnums[cur] > 0:
					lnums[cur] -= 1
					direct *= -1
					if lnums[cur] == 0:
						nzeros += 1
				cur += direct
			return nzeros == N

		return sum(isValid(i, 1) + isValid(i, -1) for i, n in enumerate(nums) if n == 0)
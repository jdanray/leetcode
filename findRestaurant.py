# https://leetcode.com/problems/minimum-index-sum-of-two-lists/

class Solution:
	def findRestaurant(self, list1, list2):
		drs = {r: i for i, r in enumerate(list1)}
		common = []
		msum = sys.maxsize
		for i, r in enumerate(list2):
			if r in drs:
				if drs[r] + i < msum:
					common = [r]
					msum = drs[r] + i
				elif drs[r] + i == msum:
					common.append(r)
		return common

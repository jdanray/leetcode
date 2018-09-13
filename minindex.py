# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution(object):
	def findRestaurant(self, list1, list2):
		minim = 2 ** 30
		common = []
		for i, r1 in enumerate(list1):
			for j, r2 in enumerate(list2):
				if r1 == r2:
					if i + j < minim:
						minim = i + j
						common = [r1]
					elif i + j == minim:
						common.append(r1)
		return minim
				

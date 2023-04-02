# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/ 

class Solution(object):
	def findMatrix(self, nums):
		count = collections.Counter(nums)
		res = []
		for n in count:
			i = 0
			while count[n] > 0:
				if i >= len(res):
					res.append([])

				res[i].append(n)
				i += 1
				count[n] -= 1

		return res

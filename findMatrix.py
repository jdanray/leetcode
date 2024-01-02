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

class Solution(object):
	def findMatrix(self, nums):
		count = collections.Counter()
		res = []
		for n in nums:
			if len(res) <= count[n]:
				res.append([])

			res[count[n]].append(n)
			count[n] += 1
                
		return res

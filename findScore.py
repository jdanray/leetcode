# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/ 

class Solution(object):
	def findScore(self, nums):
		sortedNums = sorted((n, i) for i, n in enumerate(nums))
		marked = set()
		res = 0
		for (n, i) in sortedNums:
			if i not in marked:
				res += n

				marked.add(i)
				marked.add(i - 1)
				marked.add(i + 1)
                
		return res

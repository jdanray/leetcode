# https://leetcode.com/problems/last-visited-integers/ 

class Solution(object):
	def lastVisitedIntegers(self, words):
		k = 0
		reverse_nums = []
		res = []
		for w in words:
			if w == "prev":
				k += 1
				if k <= len(reverse_nums):
					res.append(reverse_nums[-k])
				else:
					res.append(-1)
			else:
				k = 0
				reverse_nums.append(int(w))

		return res

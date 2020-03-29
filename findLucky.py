#  https://leetcode.com/problems/find-lucky-integer-in-an-array/

class Solution(object):
	def findLucky(self, arr):
		freq = collections.Counter(arr)
		res = -1
		for n in arr:
			if freq[n] == n:
				res = max(res, n)
		return res

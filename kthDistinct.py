# https://leetcode.com/problems/kth-distinct-string-in-an-array/ 

class Solution(object):
	def kthDistinct(self, arr, k):
		count = collections.Counter(arr)
		for s in arr:
			if count[s] == 1:
				k -= 1

			if k == 0:
				return s

		return ""

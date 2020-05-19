# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/ 

class Solution(object):
	def replaceElements(self, arr):
		m = -1
		res = [-1]
		for i in range(len(arr) - 2, -1, -1):
			m = max(m, arr[i + 1])
			res = [m] + res

		return res

# https://leetcode.com/problems/relative-sort-array/ 

class Solution(object):
	def relativeSortArray(self, arr1, arr2):
		count = collections.Counter(arr1)
		ans = []
		for n in arr2:
			for _ in range(count[n]):
				ans.append(n)
			count[n] = 0

		rest = []
		for n in count:
			for _ in range(count[n]):
				rest.append(n)

		return ans + rest

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

class Solution(object):
	def relativeSortArray(self, arr1, arr2):
		MAX = 1000

		count = collections.Counter(arr1)
		res = []
		for n2 in arr2:
			while count[n2] > 0:
				res.append(n2)
				count[n2] -= 1

		for n1 in range(MAX + 1):
			while count[n1] > 0:
				res.append(n1)
				count[n1] -= 1

		return res

class Solution(object):
	def relativeSortArray(self, arr1, arr2):
		idx = {a: i for i, a in enumerate(arr2)}
        
		left = [a for a in arr1 if a in idx]
		right = [a for a in arr1 if a not in idx]
        
		return sorted(left, key=lambda a: idx[a]) + sorted(right)

# https://leetcode.com/problems/find-k-closest-elements/

class Solution:
	def findClosestElements(self, arr, k, x):
		c = self.closest(arr, x)
		i = c - 1
		j = c + 1
		res = [arr[c]]
		while len(res) < k:
			if i >= 0 and (j >= len(arr) or abs(arr[i] - x) <= abs(arr[j] - x)):
				res = [arr[i]] + res
				i -= 1
			else:
				res += [arr[j]]
				j += 1
		return res

	def closest(self, arr, x):
		lo = 0
		hi = len(arr) - 1
		c = 0
		while lo <= hi:
			mid = lo + (hi - lo) // 2
			if arr[mid] == x:
				return mid

			if abs(arr[mid] - x) < abs(arr[c] - x):
				c = mid
		
			if arr[mid] < x:
				lo = mid + 1
			else:
				hi = mid - 1                
		return c	

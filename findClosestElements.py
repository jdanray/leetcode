# https://leetcode.com/problems/find-k-closest-elements/

class Solution(object):
	def findClosestElements(self, arr, k, x):
		m = float('inf')
		j = 0
		s = 0
		for i, a in enumerate(arr):
			s += abs(a - x)

			if i >= k:
				s -= abs(arr[i - k] - x)

			if i >= k - 1 and s < m:
				j = i
				m = s

		return arr[j - k + 1:j + 1]

"""
After I solve a problem, I like to study other people's solutions. I found two other solutions that I wanted to save.

The first solution comes from here: https://leetcode.com/problems/find-k-closest-elements/discuss/106426/JavaC%2B%2BPython-Binary-Search-O(log(N-K)-%2B-K)

It is a binary search for the first index i s.t. arr[i] is closer to x than arr[i + k] is. The code here is slightly different from the Python code found at the link. I have a binary search template, and I modified the code to fit the template.

The second solution comes from here: https://leetcode.com/problems/find-k-closest-elements/discuss/202785/Very-simple-Java-O(n)-solution-using-two-pointers

It is a two-pointers solution. Like the binary-search solution, it takes advantage of the fact that arr is sorted. I translated into Python the Java code found at the link.
"""

class Solution(object):
	def findClosestElements(self, arr, k, x):
		def condition(value):
			return x - arr[value] <= arr[value + k] - x

		left = 0
		right = len(arr) - k
		while left < right:
			mid = left + (right - left) // 2

			if condition(mid):
				right = mid
			else:
				left = mid + 1

		return arr[left:left + k]


class Solution(object):
	def findClosestElements(self, arr, k, x):
		i = 0
		j = len(arr) - 1
		while j - i >= k:
			if abs(arr[i] - x) > abs(arr[j] - x):
				i += 1
			else:
				j -= 1

		return arr[i:j + 1]

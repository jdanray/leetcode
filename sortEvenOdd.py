# https://leetcode.com/problems/sort-even-and-odd-indices-independently/ 

class Solution(object):
	def sortEvenOdd(self, nums):
		arr = [[], []]
		for i, n in enumerate(nums):
			arr[i % 2].append(n)

		arr[0] = sorted(arr[0])
		arr[1] = sorted(arr[1], reverse=True)

		return [arr[i % 2][i // 2] for i in range(len(nums))]

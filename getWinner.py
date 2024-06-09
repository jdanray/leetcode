# https://leetcode.com/problems/find-the-winner-of-an-array-game/

class Solution(object):
	def getWinner(self, arr, k):
		m = 0
		w = 0
		for i in range(1, len(arr)):
			if arr[i] > arr[m]:
				m = i
				w = 0

			w += 1
			if w == k:
				break

		return arr[m]

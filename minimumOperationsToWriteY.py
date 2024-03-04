# https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/ 

"""
There are six possibilities:

(1) Change the Y cells to 0s and the non-Y cells to 1s
(2) Change the Y cells to 0s and the non-Y cells to 2s
(3) Change the Y cells to 1s and the non-Y cells to 0s
(4) Change the Y cells to 1s and the non-Y cells to 2s
(5) Change the Y cells to 2s and the non-Y cells to 0s
(6) Change the Y cells to 2s and the non-Y cells to 1s

Try each possibility, and return the approach that takes the minimum number of operations. 
"""

class Solution(object):
	def minimumOperationsToWriteY(self, grid):
		N = len(grid)

		# top-left: 	i <= N//2 and j == i
		# top-right: 	i <= N//2 and j == N - i - 1
		# vertical: 	i >= N//2 and j == N//2

		ycount = collections.Counter()
		count = collections.Counter()
		ytotal = 0
		total = 0
		for i in range(N):
			for j in range(N):
				if (i <= N // 2 and (j == i or j == N - i - 1)) or (i >= N // 2 and j == N // 2):
					ycount[grid[i][j]] += 1
					ytotal += 1
				else:
					count[grid[i][j]] += 1
					total += 1

		zero = ytotal - ycount[0] + min(total - count[1], total - count[2])
		one = ytotal - ycount[1] + min(total - count[0], total - count[2])
		two = ytotal - ycount[2] + min(total - count[0], total - count[1])
        
		return min(zero, one, two)

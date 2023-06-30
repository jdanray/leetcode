# https://leetcode.com/problems/last-day-where-you-can-still-cross/ 

class Solution(object):
	def latestDayToCross(self, row, col, cells):
		deltas = [[0, -1], [0, 1], [-1, 0], [1, 0]]

		def condition(value):
			grid = [[0 for _ in range(col)] for _ in range(row)]
			for i in range(value):
				grid[cells[i][0] - 1][cells[i][1] - 1] = 1

			queue = collections.deque([])
			for j in range(col):
				if grid[0][j] == 0:
					queue.append([0, j])
					grid[0][j] = 1

			while queue:
				i, j = queue.popleft()

				if i == row - 1:
					return True

				for (di, dj) in deltas:
					ni = i + di
					nj = j + dj
                    
					if ni >= 0 and ni < row and nj >= 0 and nj < col and grid[ni][nj] == 0:
						queue.append([ni, nj])
						grid[ni][nj] = 1

			return False

		left = 1
		right = len(cells)
		while left < right:
			mid = left + (right - left) // 2

			if not condition(mid):
				right = mid
			else:
				left = mid + 1

		return left - 1

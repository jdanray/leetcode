# https://leetcode.com/problems/champagne-tower/description/

class Solution:
	def champagneTower(self, poured, query_row, query_glass):
		nextrow = [poured]
		for i in range(query_row + 1):
			row = nextrow
			nextrow = [0 for _ in range(len(row) + 1)]	
			for j, p in enumerate(row):
				if p > 1:
					excess = (p - 1) / 2
					nextrow[j] += excess
					nextrow[j + 1] += excess
					row[j] = 1
		return row[query_glass]

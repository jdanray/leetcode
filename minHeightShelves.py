# https://leetcode.com/problems/filling-bookcase-shelves/

class Solution(object):
	def minHeightShelves(self, books, shelf_width):
		memo = {}
		def dp(i):
			if i >= len(books):
				return 0
			elif i in memo:
				return memo[i]

			maxheight = 0
			width = 0
			j = i
			memo[i] = float('inf')
			while j < len(books) and width + books[j][0] <= shelf_width:
				maxheight = max(maxheight, books[j][1])
				width += books[j][0]
				j += 1
				memo[i] = min(memo[i], dp(j) + maxheight)
			return memo[i]

		return dp(0)

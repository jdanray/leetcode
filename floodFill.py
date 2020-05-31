# https://leetcode.com/problems/flood-fill/

class Solution(object):
	def floodFill(self, image, sr, sc, newColor):
		M = len(image)
		N = len(image[0])

		oldColor = image[sr][sc]

		seen = set()
		def fill(i, j):
			if i >= 0 and i < M and j >= 0 and j < N and (i, j) not in seen and image[i][j] == oldColor:
				image[i][j] = newColor
				seen.add((i, j))
                
				fill(i + 1, j)
				fill(i - 1, j)
				fill(i, j + 1)
				fill(i, j - 1)

		fill(sr, sc)
		return image

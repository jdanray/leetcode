# https://leetcode.com/problems/can-place-flowers/description/

class Solution:
	def canPlaceFlowers(self, flowerbed, n):
		i = 0
		while n > 0 and i < len(flowerbed):
			if flowerbed[i] == 1:
				while i < len(flowerbed) and flowerbed[i] == 1:
					i += 1
				i += 1
			elif i + 1 >= len(flowerbed) or flowerbed[i + 1] == 0:
				n -= 1
				i += 2
			else:
				i += 1
		return n == 0

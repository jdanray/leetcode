# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/ 

class Solution(object):
	def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
		res = 0
		foundkeys = set()
		opened = set()
		visited = set()
		while initialBoxes:
			box = initialBoxes.pop()
			visited.add(box)

			if box in opened:
				continue

			if status[box] == 1 or box in foundkeys:
				opened.add(box)
				res += candies[box]

				for cb in containedBoxes[box]:
					initialBoxes.append(cb)

				for k in keys[box]:
					foundkeys.add(k)
					if k in visited:
						initialBoxes.append(k)

		return res	

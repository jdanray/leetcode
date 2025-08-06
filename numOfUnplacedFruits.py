# https://leetcode.com/problems/fruits-into-baskets-ii/

# Time: O(M * N)
# Space: O(1)
class Solution(object):
	def numOfUnplacedFruits(self, fruits, baskets):
		placed = 0
		for f in fruits:
			for i, b in enumerate(baskets):
				if b >= f:
					placed += 1
					baskets[i] = -1
					break
		return len(fruits) - placed

# Time: O(M * N)
# Space: O(N)
class Solution(object):
	def numOfUnplacedFruits(self, fruits, baskets):
		placed = 0
		used = set()
		for f in fruits:
			for i, b in enumerate(baskets):
				if i not in used and b >= f:
					placed += 1
					used.add(i)
					break
		return len(fruits) - placed
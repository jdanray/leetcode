# https://leetcode.com/problems/check-array-formation-through-concatenation/ 

class Solution(object):
	def canFormArray(self, arr, pieces):
		N = len(arr)
		i = 0
		while i < N:
			found = False
			for piece in pieces:
				if all(arr[i + j] == p for j, p in enumerate(piece)):
					i += len(piece)
					found = True
					break
                    
			if not found:
				return False

		return True

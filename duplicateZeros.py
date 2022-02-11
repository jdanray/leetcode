# https://leetcode.com/problems/duplicate-zeros/

class Solution(object):
	def duplicateZeros(self, arr):
		N = len(arr)
		queue = collections.deque(arr)
		i = 0
		while i < N:
			n = queue.popleft()

			arr[i] = n
			i += 1

			if n == 0 and i < N:
				arr[i] = 0
				i += 1


class Solution(object):
	def duplicateZeros(self, arr):
		N = len(arr)
		queue = collections.deque(arr)
		i = 0
		while i < N:
			n = queue.popleft()
            
			for _ in range(1 + (n == 0 and i + 1 < N)):
				arr[i] = n
				i += 1

class Solution(object):
	def duplicateZeros(self, arr):
		N = len(arr)
		i = 0
		while i < N:
			if arr[i] != 0 or N <= i + 1:
				i += 1
				continue

			j = N - 1
			while j > i:
				arr[j] = arr[j - 1]
				j -= 1

			arr[i + 1] = 0
			i += 2

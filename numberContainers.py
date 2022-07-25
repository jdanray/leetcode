# https://leetcode.com/problems/design-a-number-container-system/

class NumberContainers(object):
	def __init__(self):
		self.nums = {}
		self.indexes = {}

	def change(self, index, number):
		self.nums[index] = number
		if number in self.indexes:
			heapq.heappush(self.indexes[number], index)
		else:
			self.indexes[number] = [index]
			heapq.heapify(self.indexes[number])

	def find(self, number):
		if number not in self.indexes:
			return -1

		while self.indexes[number]:
			i = heapq.heappop(self.indexes[number])
			if self.nums[i] == number:
				heapq.heappush(self.indexes[number], i)
				return i

		return -1

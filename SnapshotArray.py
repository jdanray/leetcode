# https://leetcode.com/problems/snapshot-array/ 

class SnapshotArray(object):
	def __init__(self, length):
		self.snap_id = 0
		self.snapshot = {self.snap_id: {i: 0 for i in range(length)}}

	def set(self, index, val):
		self.snapshot[self.snap_id][index] = val

	def snap(self):
		self.snap_id += 1
		self.snapshot[self.snap_id] = {}
		return self.snap_id - 1

	def get(self, index, snap_id):
		while index not in self.snapshot[snap_id]:
			snap_id -= 1
		return self.snapshot[snap_id][index]

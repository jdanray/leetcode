# https://leetcode.com/problems/frequency-tracker/ 

class FrequencyTracker(object):
	def __init__(self):
		self.count = collections.Counter()
		self.freqs = collections.Counter()

	def add(self, number):
		if self.count[number] > 0:
			self.freqs[self.count[number]] -= 1

		self.count[number] += 1
		self.freqs[self.count[number]] += 1

	def deleteOne(self, number):
		if self.count[number] > 0:
			self.freqs[self.count[number]] -= 1
			self.count[number] -= 1

		if self.count[number] > 0:
			self.freqs[self.count[number]] += 1

	def hasFrequency(self, frequency):
		return self.freqs[frequency] > 0

# https://leetcode.com/problems/maximum-frequency-stack/

import time

class FreqStack(object):
	def __init__(self):
		self.stack = []
		self.freq = collections.defaultdict(int)

	def push(self, x):
		self.freq[x] += 1
		heapq.heappush(self.stack, (-self.freq[x], -time.time(), x))
	
	def pop(self):
		f, t, x = heapq.heappop(self.stack)
		self.freq[x] -= 1
		return x

"""
After I solve a problem, I like to examine other people's solution. Here is a nice solution: https://leetcode.com/problems/maximum-frequency-stack/discuss/163410/C%2B%2BJavaPython-O(1)

I give you my Python implementation of the above idea: 
"""

class FreqStack(object):
	def __init__(self):
		self.maxfreq = 0
		self.freq = collections.defaultdict(int)
		self.m = collections.defaultdict(list)

	def push(self, x):
		self.freq[x] += 1
		self.maxfreq = max(self.maxfreq, self.freq[x])
		self.m[self.freq[x]].append(x)
	
	def pop(self):
		x = self.m[self.maxfreq].pop()
		if not self.m[self.freq[x]]:
			self.maxfreq -= 1
            
		self.freq[x] -= 1
		return x

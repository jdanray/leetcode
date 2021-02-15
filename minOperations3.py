# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

class Solution(object):
	def minOperations(self, s):
		start0 = 0
		for i, c in enumerate(s):
			if i % 2 == 0 and c != '0':
				start0 += 1
			elif i % 2 == 1 and c != '1':
				start0 += 1

		start1 = 0		
		for i, c in enumerate(s):
			if i % 2 == 0 and c != '1':
				start1 += 1
			elif i % 2 == 1 and c != '0':
				start1 += 1

		return min(start0, start1)

class Solution(object):
	def minOperations(self, s):
		start0 = 0
		start1 = 0		
		for i, c in enumerate(s):
			if i % 2 == 0 and c != '0':
				start0 += 1
			elif i % 2 == 1 and c != '1':
				start0 += 1

			if i % 2 == 0 and c != '1':
				start1 += 1
			elif i % 2 == 1 and c != '0':
				start1 += 1

		return min(start0, start1)

class Solution(object):
	def minOperations(self, s):
		start0 = 0
		start1 = 0		
		for i, c in enumerate(s):
			if i % 2 == 0: 
				if c == '0':
					start1 += 1
				else: 
					start0 += 1
			elif i % 2 == 1:
				if c == '0':
					start0 += 1
				else:
					start1 += 1

		return min(start0, start1)

class Solution(object):
	def minOperations(self, s):
		start0 = 0
		start1 = 0		
		for i, c in enumerate(s):
			if i % 2 == 0: 
				if c == '0':
					start1 += 1
				else: 
					start0 += 1
			elif c == '0':
				start0 += 1
			else:
				start1 += 1

		return min(start0, start1)

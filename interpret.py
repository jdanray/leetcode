# https://leetcode.com/problems/goal-parser-interpretation/ 

class Solution(object):
	def interpret(self, command):
		i = 0
		res = ''
		while i < len(command):
			if command[i] == 'G':
				res += 'G'
				i += 1
			elif command[i + 1] == ')':
				res += 'o'
				i += 2
			else:
				res += 'al'
				i += 4
		return res

class Solution(object):
	def interpret(self, command, i=0):
		if i >= len(command):
			return ''
		elif command[i] == 'G':
			return 'G' + self.interpret(command, i + 1)
		elif command[i + 1] == ')':
			return 'o' + self.interpret(command, i + 2)
		else:
			return 'al' + self.interpret(command, i + 4)

# https://leetcode.com/problems/fizz-buzz/description/

class Solution:
	def fizzBuzz(self, n):
		output = []
		for num in range(1, n + 1):
			if num % 3 == 0 and num % 5 == 0:
				output.append("FizzBuzz")
			elif num % 3 == 0:
				output.append("Fizz")
			elif num % 5 == 0:
				output.append("Buzz")
			else:
				output.append(str(num))
		return output

# https://leetcode.com/problems/defuse-the-bomb/

# Quadratic time 

class Solution(object):
	def decrypt(self, code, k):
		N = len(code)
		res = [0 for _ in range(N)]
		for i, c in enumerate(code):
			if k < 0: 
				res[i] = sum(code[j % N] for j in range(i + k, i))
			else:
				res[i] = sum(code[j % N] for j in range(i + 1, i + 1 + k))
		return res

# Linear time
# So that you don't have to re-compute the sums at each iteration, maintain a running sum

class Solution(object):
	def decrypt(self, code, k):
		N = len(code)

		if k < 0:
			s = sum(code[j % N] for j in range(k, 0))
		else:
			s = sum(code[j % N] for j in range(0, k))

		tail = k % N
		res = [0 for _ in range(N)]
		for i, c in enumerate(code):
			if k < 0:
				res[i] = s
				s -= code[tail]
				s += c
			else:
				s += code[tail]
				s -= c
				res[i] = s

			tail += 1
			tail %= N

		return res

"""
After I solve problems, I like to examine other people's solutions

The following is my Python implementation of a linear-time program written in Java. You can see the original program here: https://leetcode.com/problems/defuse-the-bomb/discuss/935398/JAVA-o(n)-100-time-and-space-short-and-concise-sliding-window

My linear-time program maintained a 'tail' variable. This program maintains both 'head' and 'tail' variables. That enables the code to be simpler.
"""
 
class Solution(object):
	def decrypt(self, code, k):
		N = len(code)

		if k < 0:
			start = 1
			end = k
		else:
			start = N + k
			end = N - 1

		s = sum(code[i] for i in range(start, end + 1))
		res = [0 for _ in range(N)]
		for i range(N):
			res[i] = s

			s -= code[start % N]
			start += 1

			end += 1
			s += code[end % N]

		return res

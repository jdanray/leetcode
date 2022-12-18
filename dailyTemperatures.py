# https://leetcode.com/problems/daily-temperatures/

"""
---------------------------------------------
Analysis of the problem
---------------------------------------------
1) Preconditions

T is a list of N ints

2) Postconditions

For every 0 <= i < N,
	wait[i] == 0, if there's no j > i such that T[j] > T[i]
	wait[i] == j - i, for the closest j > i such that T[j] > T[i]
--------------------------------------------------------
Thoughts on the problem
--------------------------------------------------------
The first thing I do is modify the problem. That is, I try to solve a different problem. This problem will turn out to be a subproblem of the original, main problem.

Right now I don't want to know the "distance" between the ith day and the nearest warmer day. Instead I want to know the index of the nearest warmer day. This information will make finding the nearest warmer day a lot easier. So, I want to establish this proposition instead:

For every 0 <= i < N,
	wait[i] == i, if there's no j > i such that T[j] > T[i]
	wait[i] == j, for the closest j > i such that T[j] > T[i]

To help with this, I initialize wait so that wait[i] == i for all i. By default, we leave wait[i] as it is. But if there is some j > i such that T[j] > T[i], we modify wait[i] so that it equals j. So, for each 0 <= i < N, I need to determine whether there is some N >= j > i such that T[j] > T[i].

The new problem is almost exactly the same as the original problem. All I need to do is solve it and modify its solution, and then I have a solution to the original problem. And solving the new problem is a lot easier than solving the original problem.

Focusing on the new problem, now the main goal is to define/clarify wait[i] in every case. There are two cases:

(1) T[i + 1] > T[i]
(2) T[i + 1] <= T[i]

(The two cases correspond to a base case and an inductive step.)

Consider (1). If the immediately successive integer is greater, then wait[i] = i + 1.

Now consider (2). If the immediately successive integer isn't greater, then examine wait[i + 1]. We know that wait[i + 1] corresponds to a temperature that is greater than T[i + 1]. But T[i + 1] <= T[i]. So, T[wait[i + 1]] might not be greater than T[i]. So, while it isn't, we search through the "local maxima" until we either find one greater than T[i] or learn that there isn't one.

At the end of that iteration, we've established the truth of the proposition we wanted to establish; wait[i] has the property that we wanted it to, for all 0 <= i < N.

But that is only the property that we wanted it to have in the intermediate. I established that property because it was easier to establish, and now I can use it to find what I really wanted, to achieve my ultimate objective. I do that easily by computing wait[i] - i for all i. Now the postcondition is true.
"""

class Solution:
	def dailyTemperatures(self, T):
		wait = [i for i in range(len(T))]
		for i in range(len(T) - 2, -1, -1):
			if T[i + 1] > T[i]:
				wait[i] = i + 1
				continue

			j = i + 1
			while wait[j] != j and T[wait[j]] <= T[i]:
				j = wait[j]
	
			if T[wait[j]] > T[i]:
				wait[i] = wait[j]

		return [w - i for i, w in enumerate(wait)]

"""
In spite of my above analysis, there is a much more straightforward solution to the problem. 

In fact, this is a classic monostack problem. 

Here is the solution:
"""

class Solution(object):
	def dailyTemperatures(self, temperatures):
		N = len(temperatures)
        
		res = [0 for _ in range(N)]
		stack = []
		for i in range(N - 1, -1, -1):
			while stack and temperatures[stack[-1]] <= temperatures[i]:
				stack.pop()

			if stack:
				res[i] = stack[-1] - i
 
			stack.append(i)

		return res

# There is an even better stack solution:

class Solution(object):
	def dailyTemperatures(self, temps):
		res = [0 for _ in range(len(temps))]
		stack = []
		for i, t in enumerate(temps):
			while stack and t > temps[stack[-1]]:
				j = stack.pop()
				res[j] = i - j
                
			stack.append(i)
            
		return res 

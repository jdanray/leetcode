# https://leetcode.com/problems/soup-servings/

"""
-----------------------------------------
Preconditions:

N is a given number
N <= 0 <= 10**9
A == N
B == N
operations == [[100, 0], [75, 25], [50, 50], [25, 75]]
-----------------------------------------
Postconditions:

P == p(A is empty first) + 0.5 * p(A and B become empty at the same time)
-----------------------------------------
Thoughts:

>We stop once we no longer have some quantity of both types of soup.

I immediately thought that the algorithm that solves this problem will be top-down and recursive. The above sentence told me what the base case is: A == 0 or B == 0.

But the base case consists of three [3] "sub-cases", each of which corresponds to a value of P:

1) Both A == 0 and B == 0

p(A is empty first) == 0
p(A and B become empty at the same time) == 1
Therefore, P == 0 + 0.5 * 1 == 0.5

2) Only A == 0

p(A is empty first) == 1
p(A and B become empty at the same time) == 0
Therefore, P == 1 + 0.5 * 0 == 1

3) Only B == 0

p(A is empty first) == 0
p(A and B become empty at the same time) == 0
Therefore, P == 0 + 0.5 * 0 == 0

Now let's consider the inductive case:

In general, if a problem instance isn't a base case, then we'll want to reduce the size of the problem instance. In this problem, we have four ways to reduce the size of a problem instance available to us. We perform each operation and then recurse on the new, smaller problem instance. Then, since all of the four operations are equally likely to occur, we multiply the sum of our subsolutions by 0.25.
-----------------------------------------
I thought out all of the above and implemented my ideas. My program worked for small values of N, which was encouraging, but it was too slow for large values. I tried memoization, and memoization sped the program up. The program worked on larger values of N. However, it was still too slow. I worried that my thinking was wrong. I checked leetcode's solution [https://leetcode.com/problems/soup-servings/solution/]. 

I think that I was fundamentally correct, but the problem features a trick. The trick was to pay close attention to this part of the problem statement:

>we do not have the operation where all 100 ml's of soup B are used first.  

This means that p(A is empty first) approaches 1 as N grows. In fact, it turns out that, after N >= 4800, you can always just return 1, thanks to this other fact expressed in the problem statement:

>Answers within 10^-6 of the true value will be accepted as correct.
-----------------------------------------
"""

class Solution(object):
	def soupServings(self, N):
		if N >= 4800:
			return 1

		memo = {}
		operations = [[100, 0], [75, 25], [50, 50], [25, 75]]
		def helper(A, B):
			if (A, B) in memo:
				return memo[A, B]

			if A == 0 and B == 0:
				return 0.5
			elif A == 0:
				return 1
			elif B == 0:
				return 0

			memo[A, B] = 0.25 * sum(helper(A - min(A, op[0]), B - min(B, op[1])) for op in operations)
			return memo[A, B]
        
		return helper(N, N)

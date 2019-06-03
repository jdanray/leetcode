# https://leetcode.com/problems/reordered-power-of-2/

"""
Preconditions:

N is a positive integer
1 <= N <= 10**9

Postconditions:

RESULT is true iff the digits of N can be ordered to form a number N2 that is a power of 2
N2 may NOT have a leading digit of 0

Thoughts:

A positive integer N is a power of 2 iff there exists a nonnegative integer k such that 2 ** k == N.

Do I want to represent N as a list, st 1234 becomes [1,2,3,4]? It depends on the operations that I want to perform. And the operations that I'll want to perform will depend on the states that I want to reach.

A brute-force search will test every permutation of a given N. Because N <= 10**9, that means that the time-complexity of the algorithm will be O(10!). 

What's a craftier way than brute-force? I need to understand the problem better. Instead of applying a general algorithm, I want to find some structure particular to the problem.

Update:

I tried to find a pattern in numbers that are powers of 2. So, I opened python and looked at examples of powers of 2:

for k in range(21):
     print('2 ** %i == %i' % (k, 2 ** k))

I realized that there's only a handful of powers of 2 that are l.t.e. 10**9 (our upper limit on N). So, I thought that I could save them all and then, for any given N, check whether N can be formed into one of them. Doing that check is easy. P1 can be rearranged into P2 iff the count of P1's elements is equal to the count of P2's elements (ie, collections.Counter(P1) == collections.Counter(P2)). So, I can just count and compare.

After my solution was accepted, I looked at other people's solutions. The top-voted solution implemented the same algorithm that I arrived at [Source: https://leetcode.com/problems/reordered-power-of-2/discuss/149843/C%2B%2BJavaPython-Straight-Forward].

I have mixed feelings about that. I like that my solution resembled the solution of a good problem-solver, but I am afraid that people will think that I stole their solution, and I feel frustrated since producing the same solution as somebody else shows that I am not "thinking outside of the box" too much. But, then again, there are limits to thinking outside of the box. For any given problem, there are only so many approaches that will actually work. 
"""

class Solution(object):
	def __init__(self):
		upper = 10 ** 9
		p = 1
		powers = []
		while p <= upper:
			powers.append(p)
			p *= 2

		self.counts = [collections.Counter(str(p)) for p in powers] 

	def reorderedPowerOf2(self, N):
		return collections.Counter(str(N)) in self.counts

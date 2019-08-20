# https://leetcode.com/problems/rotate-function/

"""
To get F0:		Compute i*A[i], for i=0,1,...,N-1, and sum the products
To get F1 from F0:	Subtract (N-1)*6, Add 4,3,2
F1->F2:			Subtract (N-1)*2, Add 6,4,3
F2->F3:			Subtract (N-1)*3, Add 2,6,4

To get F1 from F0:	Subtract (N-1)*A[N-1], Add A[0],A[1],A[2]
F1->F2:			Subtract (N-1)*A[N-2], Add A[N-1],A[0],A[1]
F2->F3:			Subtract (N-1)*A[N-3], Add A[N-2],A[N-1],A[0]
"""

class Solution(object):
	def maxRotateFunction(self, A):
		N = len(A)
		add = sum(A[:-1])
		F = sum(i * a for i, a in enumerate(A))
		res = F
		for k in range(1, N):
			sub = (N - 1) * A[N - k]
			F -= sub
			F += add 
			res = max(res, F)
			add -= A[N - k - 1]
			add += A[N - k]
		return res

"""
After I solve problems, I like to examine solutions given by other people.

I discovered my solution by studying the specific example that leetcode gives. The leetcode contributor "oreomilkshake" offers a general analysis:

	F(k)	= 0 * Bk[0] 	+ 1 * Bk[1] 	+  ... 	+ (n-1) * Bk[n-1]
	F(k-1)	= 0 * Bk-1[0] 	+ 1 * Bk-1[1] 	+  ... 	+ (n-1) * Bk-1[n-1]
		= 0 * Bk[1] 	+ 1 * Bk[2] 	+  ... 	+ (n-2) * Bk[n-1] + (n-1) * Bk[0]
	Then,
	F(k) - F(k-1)	= Bk[1] + Bk[2] + ... + Bk[n-1] + (1-n)Bk[0]
			= (Bk[0] + ... + Bk[n-1]) - nBk[0]
			= sum - nBk[0]
	Thus,
	F(k) = F(k-1) + sum - nBk[0]

	What is Bk[0]?
	k = 0; B[0] = A[0];
	k = 1; B[0] = A[len-1];
	k = 2; B[0] = A[len-2];
	...

The above analysis leads to a simpler, faster solution:

	int allSum = 0;
	int len = A.length;
	int F = 0;
	for (int i = 0; i < len; i++) {
		F += i * A[i];
		allSum += A[i];
	}
	int max = F;
	for (int i = len - 1; i >= 1; i--) {
		F = F + allSum - len * A[i];
		max = Math.max(F, max);
	}
	return max;  

(See: https://leetcode.com/problems/rotate-function/discuss/87853/Java-O(n)-solution-with-explanation)

The algorithm in Python:

	N = len(A)
	add = sum(A)
	F = sum(i * a for i, a in enumerate(A))
	res = F
	for i in range(N - 1, 0, -1):
		F += add - N * A[i]
		res = max(res, F)
	return res

I am still proud of my solution, but I can't wait until I think more abstractly. I saw that you want to compute F(k) from F(k-1), but I wish that I had thought of the problem in more general terms.

Onwards and upwards.
"""

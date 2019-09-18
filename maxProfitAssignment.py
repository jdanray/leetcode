# https://leetcode.com/problems/most-profit-assigning-work/

"""
Input:

There are M jobs and N workers.

We use two arrays to represent the jobs:

	profit[i] represents the profit of the i-th job.
	difficulty[i] represents the difficulty of the i-th job.

We use one array to represent the workers:

	worker[i] represents the ability of the i-th worker
		The i-th worker can complete the j-th job only if difficulty[j] <= worker[i]. 

1 <= M <= 10**4
1 <= N <= 10**4
1 <= difficulty[i] <= 10**5
1 <= profit[i] <= 10**5
1 <= worker[i] <= 10**5

Output:

We try to assign each worker some job. Let paid[i] represent the profit that the i-th worker receives from their job. We can assign different workers the same job. 

Let paid have the same length as worker. (Ie, len(paid) == len(worker) == N.)  

Objective: Maximize sum(paid).

Constraints: 

Why don't I just set paid[i] == max(profit) for all i? Because the i-th worker can't receive profit[j] if difficulty[j] > worker[i]. You must maximize sum(paid) under that constraint.

In other words, for each 0 < i < N, we search for some 0 < j < M such that 
	difficulty[j] <= worker[i] 
	profit[j] >= profit[k] for all 0 < k < M

We assume that the problem has optimal substructure, because it obviously does. If we ever choose profit[j] < profit[k], then we'll have a suboptimal solution.

How fast does the algorithm have to be? There could be a case where both M == 10**4 and N == 10**4. So, it seems that O(M * N) is too slow.

The obvious, brute-force solution looks like this:

	paid = 0
	for i in 0..N
		p = 0
		for j in O..M
			if difficulty[j] <= worker[i]
				p = max(p, profit[j])
		paid += p
	return paid			

It seems like the solution must be at least O(N). At any rate, the obvious idea is to consider each of the N workers, trying to find the most profitable job for each. In that case, the trick is to speed up that search. Maybe a binary search will do the trick. Then the algorithm becomes O(N * log(M)). That should be fast enough.

We search through difficulty, rather than profit.

First of all, we sort difficulty. This means that the algorithm is at least O(M*log(M)).

Then, for each difficulty[i], we find the maximum profit among all jobs that are equally or less difficult. This is O(M).

Now, for each worker[i], we find the maximum difficulty level for all jobs that the i-th worker can complete. That will ensure, for each worker, we find the most profit that the worker can achieve. This is O(N * log(M)).
"""

class Solution(object):
	def maxProfitAssignment(self, difficulty, profit, worker):
		M = len(difficulty)
		jobs = sorted(zip(difficulty, profit))
		maxp = [0 for _ in range(M)]
		maxp[0] = jobs[0][1]
		for i in range(1, M):
			maxp[i] = max(maxp[i - 1], jobs[i][1])

		ds = [j[0] for j in jobs]
		paid = 0
		for w in worker:
			i = bisect.bisect_right(ds, w)
			if i > 0:
				paid += maxp[i - 1]

		return paid

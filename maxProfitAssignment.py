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

"""
I did all of the above on 9/17/2019. It is 6/17/2024 now. I thought about this problem VERY differently today. 

I see that my old idea was this: For each worker w, find w the most profitable job that w can complete. So, I iterated over workers, and, for each worker, I did a binary search to find a job that satisfied the criterion. 

Today, I noticed/observed that the same job can be completed multiple times, and my immediate intuition was this: Look at the absolute most profitable job. Assign it to as many workers as possible. (To that end, consider the ablest workers first: The ablest worker is most likely to be able to complete a job.)

So, my first thought was a greedy algorithm: Sort the jobs in decreasing order by profit. Sort the workers in decreasing order by ability. Try to assign the first job to the first worker. If the first job is too difficult for him, it will also be too difficult for every other worker: This first worker is the ablest worker, as the workers are sorted by ability. So, ignore that job, and move onto the second most profitable job.

Even though you might skip jobs, future workers can't miss out on previous, more profitable jobs, because the workers are sorted by ability. So, if a future worker can complete a job, then all the previous workers can, as well. So, they will do that job themselves. That job won't get skipped over. 

With the old idea, the emphasis was on the workers: For each worker, find him the most profitable job possible. With the current idea, the focus is on jobs: Take the most profitable job, and assign it to the maximum number of workers.

Here is the new program. I believe that it is simpler:
"""

class Solution(object):
	def maxProfitAssignment(self, difficulty, profit, worker):
		M = len(profit)
		N = len(worker)

		jobs = sorted(zip(profit, difficulty), reverse=True)
		worker = sorted(worker, reverse=True)

		i = 0
		j = 0
		res = 0
		while i < M and j < N:
			if worker[j] >= jobs[i][1]:
				res += jobs[i][0]
				j += 1
			else:
				i += 1

		return res 

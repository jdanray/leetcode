# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/ 

"""
If k == 1, then the problem is easy. Check whether nums[i] == nums[i+1] + 1 for each 0 <= i < len(nums) - 1. Return true iff that condition holds.

If len(nums) == 1, then the problem is easy. We are guaranteed that 1 <= k <= len(nums). So, k == 1. Return true.

What if len(nums) == 2 and k == 2? Return true.

Return true whenever len(nums) == k.

What if len(nums) > k? 

We are guaranteed that k >= 1. So, in the case where len(nums) > k, len(nums) > 1.

In every case, no set is larger than len(nums) / k. 

First idea: We consider nums[0]. We imagine a set and put nums[0] into it. We determine whether there is a nums[i] such that nums[i] == nums[0] + 1. If there is, then we might want to add it to our set. But the difficulty is that we might not. We might want it to be the "head" of another set or a "link" in the "chain" of another set. But if the size of the current set would be made greater than len(nums) / k, then we definitely don't want to add the nums[i] to the current set, because no set can be larger than len(nums) / k.

Another idea: Count the elements of nums. Then consider any nums[i]. If count[nums[i] + 1] == 0, then nums[i] must be the "tail" of any set that it belongs to. Say that count[nums[i] + 1] > 0. If count[nums[i] + 1] > count[nums[i]], then the number of sets that begin with nums[i] + 1 as the "head" must be equal to count[nums[i] + 1] - count[nums[i]], because that many instances of nums[i] + 1 can't be a consecutive "link". What if count[nums[i] + 1] == count[nums[i]]? What if count[nums[i] + 1] < count[nums[i]]? Does it matter? 

I want to find the right issue to "split" on. I ask the right question. I consider each possible answer. For each case, I maintain some invariant. The invariant here is something like "So far I haven't been able to rule out that nums can be divided into sets of k consecutive numbers". (Of course, if that is the invariant, then at the end of the iteration, I can only conclude that I haven't been able to rule out that nums can be divided into sets of k consecutive numbers. So I haven't decided whether nums actually can be so divided. So, this isn't the invariant exactly. But the invariant is something like this.)

[The "right" issue is a question that enables me to (easily) maintain the appropriate invariant(s) in every case.] 

I misunderstood the problem! I thought that there was supposed to be k sets. No. Each set must have length k. There can be any number of sets. 

This problem just got easier.

[NOTE: I would have been more likely to have understood the problem correctly if I had (1) studied the given statement of the problem [In fact, I just glanced over it], (2) stated the problem in my own words, and (3) analyzed the problems (into preconditions/inputs, postconditions/outputs, etc). 

Case k == 1 is still easy. In fact, it is trivial now. If k == 1, then just return true, no matter what nums is equal to.

If k == len(nums), then we can solve the problem by checking whether nums[i] == nums[i+1] + 1 for each 0 <= i < len(nums) - 1. Return true iff that condition holds.

First idea: Consider nums[0]. Determine whether count[nums[i] + 1] >= count[nums[0]], for 0 <= i < k - 1. If there is some nums[i] such that count[nums[i] + 1] < count[nums[0]], then return false. For each nums[i], decrement count[nums[i]] by count[nums[0]].

Maybe the following will work. Count the elements of nums: Place nums into a counter. Sort the counter's keys. For each key, consider count[key]. Say that count[key] > 0. Then we need[?] to know whether count[n] >= count[key] for key < n < key + k. 

This solution might be too slow.
"""

class Solution(object):
	def isPossibleDivide(self, nums, k):
		count = collections.Counter(nums)
		for head in sorted(count.keys()):
			if count[head] == 0:
				continue

			for n in range(head + 1, head + k):
				if count[n] < count[head]:
					return False
				else:
					count[n] -= count[head]

		return True

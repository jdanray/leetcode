# https://leetcode.com/problems/find-subarray-with-bitwise-and-closest-to-k/ 

# cleaned-up program
class Solution(object):
	def minimumDifference(self, nums, k):
		bits = collections.Counter()
		def modify(n, i, j, add):
			b = 0
			while n > 0:
				if add == 1:
					bits[b] += n & 1
				else:
					bits[b] -= n & 1
				b += 1
				n >>= 1

			sub = 0
			for b in bits:
				if bits[b] == j - i + add:
					sub += (1 << b)
			return sub
			
		i = 0
		res = float('inf')
		for j, n in enumerate(nums):
			sub = modify(n, i, j, 1)
			res = min(res, abs(sub - k))

			while i < j and sub < k:
				sub = modify(nums[i], i, j, 0)
				res = min(res, abs(sub - k))
				i += 1

		return res

# original program
class Solution(object):
	def minimumDifference(self, nums, k):
		bits = collections.Counter()
		i = 0
		res = float('inf')
		for j, n in enumerate(nums):
			# AND
			m = n
			b = 0
			while m > 0:
				bits[b] += m & 1
				b += 1
				m >>= 1

			sub = 0
			for b in bits:
				if bits[b] == j - i + 1:
					sub += (1 << b)

			if sub == k:
				return 0

			res = min(res, abs(sub - k))

			while i < j and sub < k:
				m = nums[i]
				b = 0
				while m > 0:
					bits[b] -= m & 1
					b += 1
					m >>= 1

				sub = 0
				for b in bits:
					if bits[b] == j - i:
						sub += (1 << b)

				res = min(res, abs(sub - k))
				i += 1

		return res

"""
After I solve a problem, I like to study other people's solutions. My solution is just like this one: https://leetcode.com/problems/find-subarray-with-bitwise-and-closest-to-k/discuss/5243400/Sliding-window-with-frequency-counter

However, this solution is simpler and more efficient: https://leetcode.com/problems/find-subarray-with-bitwise-and-closest-to-k/discuss/5243477/Most-simple-solution-with-set-operations-O(30n)-beats-100

I implemented this new solution in Python:
"""

class Solution(object):
	def minimumDifference(self, nums, k):
		cur = set()
		res = float('inf')
		for n in nums:
			cur = {n} | {c & n for c in cur}
			res = min(res, min(abs(c - k) for c in cur))
		return res

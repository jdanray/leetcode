# https://leetcode.com/problems/maximum-length-of-repeated-subarray/

class Solution(object):
	def findLength(self, A, B):
		M = 0
		memo = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
		for i in range(len(A) - 1, -1, -1):
			for j in range(len(B) - 1, -1, -1):
				if A[i] == B[j]:
					memo[i][j] = 1 + memo[i + 1][j + 1]
					M = max(M, memo[i][j]) 
		return M

class Solution(object):
	def findLength(self, nums1, nums2):
		M = len(nums1)
		N = len(nums2)

		def condition(value):
			s1 = collections.deque([])
			subs = set()
			for n1 in nums1:
				s1.append(n1)
				if len(s1) == value:
					subs.add(tuple(s1))
					s1.popleft()

			s2 = collections.deque([])
			for n2 in nums2:
				s2.append(n2)
				if len(s2) == value:
					if tuple(s2) in subs:
						return True
					s2.popleft()

			return False

		left = 1
		right = min(M, N)
		while left <= right:
			mid = left + (right - left) // 2

			if condition(mid):
				left = mid + 1
			else:
				right = mid - 1

		return right

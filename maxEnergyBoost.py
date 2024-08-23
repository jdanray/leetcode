# https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/ 

class Solution(object):
	def maxEnergyBoost(self, A, B):
		N = len(A)

		# mA[i] is the max energy boost you can receive up to the i-th hour, given that you choose drink A in the i-th hour
		# mB[i] is the max energy boost you can receive up to the i-th hour, given that you choose drink B in the i-th hour
		# res is the max energy boost you can receive up to the i-th hour
		mA = [0 for _ in range(N)]
		mB = [0 for _ in range(N)]
		res = 0
		for i in range(N):
			mA[i] = A[i]
			mB[i] = B[i]

			# don't switch drinks
			if i - 1 >= 0:
				mA[i] += mA[i - 1]
				mB[i] += mB[i - 1]

			# switch drinks
			if i - 2 >= 0:
				mA[i] = max(mA[i], mB[i - 2] + A[i])
				mB[i] = max(mB[i], mA[i - 2] + B[i])

			res = max(mA[i], mB[i])

		return res

# O(1) space
class Solution(object):
	def maxEnergyBoost(self, A, B):
		N = len(A)

		mA, mA1, mA2 = 0, 0, 0
		mB, mB1, mB2 = 0, 0, 0
		res = 0
		for i in range(N):
			mA = A[i]
			mB = B[i]

			# don't switch drinks
			if i - 1 >= 0:
				mA += mA1
				mB += mB1

			# switch drinks
			if i - 2 >= 0:
				mA = max(mA, mB2 + A[i])
				mB = max(mB, mA2 + B[i])

			res = max(mA, mB)

			mA1, mA2 = mA, mA1
			mB1, mB2 = mB, mB1

		return res

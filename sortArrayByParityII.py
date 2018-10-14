# https://leetcode.com/contest/weekly-contest-106/problems/sort-array-by-parity-ii/

class Solution(object):
	def sortArrayByParityII(self, A):
		odd = []
		even = []
		for a in A:
			if a % 2 == 1:
				odd.append(a)
			else:
				even.append(a)

		o = 0
		e = 0
		for i in range(len(A)):
			if i % 2 == 1:
				A[i] = odd[o]
				o += 1
			else:
				A[i] = even[e]
				e += 1

		return A

# https://leetcode.com/problems/most-frequent-prime/ 

class Solution(object):
	def mostFrequentPrime(self, mat):
		dxy = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]] 
		m = len(mat)
		n = len(mat[0])

		def isPrime(num):
			rt = num ** 0.5
			i = 2
			while i <= rt:
				if num % i == 0:
					return False
				i += 1
			return True

		count = collections.defaultdict(int)
		maxc = 0
		res = -1
		for i in range(m):
			for j in range(n):
				for d in range(len(dxy)):
					x = i
					y = j
					num = 0
					while x >= 0 and x < m and y >= 0 and y < n:
						num *= 10
						num += mat[x][y]
                        
						if num > 10 and isPrime(num):
							count[num] += 1
							if count[num] > maxc or (count[num] == maxc and num > res):
								maxc = count[num]
								res = num

						x += dxy[d][0]
						y += dxy[d][1]

		return res

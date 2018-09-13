# https://leetcode.com/problems/add-binary/description/

class Solution:
	table = {'': {}, '0': {}, '1': {}}

	table[''][''] = [('', 0), ('1', 0)]
	table['']['0'] = [('0', 0), ('1', 0)]
	table['']['1'] = [('1', 0), ('0', 1)]
	table['0'][''] = [('0', 0), ('1', 0)]
	table['0']['0'] = [('0', 0), ('1', 0)]
	table['0']['1'] = [('1', 0), ('0', 1)]
	table['1'][''] = [('1', 0), ('0', 1)]
	table['1']['0'] = [('1', 0), ('0', 1)]
	table['1']['1'] = [('0', 1), ('1', 1)]

	def addBinary(self, a, b):
		i = len(a)
		j = len(b)
		s = ''
		carry = 0
		while i > 0 or j > 0:
			i -= 1
			j -= 1

			m = '' if i < 0 else a[i]
			n = '' if j < 0 else b[j]
		
			bit, carry = self.table[m][n][carry]
			s = bit + s

		if carry:
			s = '1' + s

		return s

a = '10110'
b = '11'
soln = Solution()
print(soln.addBinary(a, b))

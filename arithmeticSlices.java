# https://leetcode.com/problems/arithmetic-slices/description/

class Solution {
	public int numberOfArithmeticSlices(int[] A) {
		int i = 0;
		int nslices = 0;
		while (i <= A.length - 3) {
			int k = 0;
			int d = A[i + 1] - A[i];
			for (int j = i + 1; j < A.length - 1; j++) {
				if (A[j + 1] - A[j] != d) 
					break;
				k++;
				nslices += k;
			}

			i += k + 1;  
		}

		return nslices;
	}
}

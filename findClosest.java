// https://leetcode.com/problems/find-closest-person/

class Solution {
	public int findClosest(int x, int y, int z) {
		int one = Math.abs(x - z);
		int two = Math.abs(y - z);

		if (one < two)
			return 1;
		else if (two < one)
			return 2;
		else 
			return 0;
	}
}
// https://leetcode.com/problems/longest-continuous-increasing-subsequence/

class Solution {
	public int findLengthOfLCIS(int[] nums) {
		int N = nums.length;

		int l = 0;
		int m = 0;
		int i = 0;

		while (i != N) {
			if (i > 0 && nums[i] > nums[i - 1])
				l++;
			else
				l = 1;

			m = Math.max(m, l);
			i++;
		}

		return m;
	}
}

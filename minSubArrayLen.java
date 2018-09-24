# https://leetcode.com/problems/minimum-size-subarray-sum/description/

class Solution {
	public int minSubArrayLen(int s, int[] nums) {
		int minlen = nums.length + 1;
		for (int i = 0; i < nums.length; i++) {
			int subsum = 0;
			for (int j = i; j < nums.length; j++) {
				subsum += nums[j];
				if (subsum >= s) {
					minlen = min(minlen, j - i + 1);
					break;
				}
			}
		}

		if (minlen == nums.length + 1)
			minlen = 0;
		return minlen;
	}
}

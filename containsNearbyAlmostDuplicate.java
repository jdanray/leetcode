/*
 * NOTE: This is NOT my solution
 * My solution is listed at containsNearbyAlmostDuplicate.py
 * After I solve a problem, I like to study other people's solutions
 * This one was too good not to preserve
 * It uses minimal code, and the code is simple
 * It achieves this by using a smart data structure (in this case, a TreeSet)
 * (Unfortunately, Python doesn't have treesets, or I'd implement this algorithm myself)
 * For more, see:
 * https://leetcode.com/problems/contains-duplicate-iii/discuss/61655/Java-O(N-lg-K)-solution
 */

public class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if (nums == null || nums.length == 0 || k <= 0) {
            return false;
        }

        final TreeSet<Integer> values = new TreeSet<>();
        for (int ind = 0; ind < nums.length; ind++) {

            final Integer floor = values.floor(nums[ind] + t);
            final Integer ceil = values.ceiling(nums[ind] - t);
            if ((floor != null && floor >= nums[ind])
                    || (ceil != null && ceil <= nums[ind])) {
                return true;
            }

            values.add(nums[ind]);
            if (ind >= k) {
                values.remove(nums[ind - k]);
            }
        }

        return false;
    }
}

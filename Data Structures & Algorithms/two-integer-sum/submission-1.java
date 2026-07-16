class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[][] pair = new int[nums.length][2];
        for (int i = 0; i < nums.length; i++) {
            pair[i][0] = nums[i];
            pair[i][1] = i;
        }
        Arrays.sort(pair, (a, b) -> Integer.compare(a[0], b[0]));
        int lPtr = 0;
        int rPtr = nums.length - 1;
        while(lPtr<rPtr){
            int sum = pair[lPtr][0] + pair[rPtr][0];
            if (sum==target){
                int i = pair[lPtr][1];
                int j = pair[rPtr][1];
                return new int[]{Math.min(i, j), Math.max(i, j)};
            } else if (sum < target){
                lPtr++;
            } else {
                rPtr--;
            }
        }
        return new int[2];
    }
}

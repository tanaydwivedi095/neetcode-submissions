class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet();
        for(int idx=0; idx<nums.length; idx++){
            if (set.contains(nums[idx])){
                return true;
            } else {
                set.add(nums[idx]);
            }
        }
        return false;
    }
}
class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap <Integer, Boolean> values = new HashMap<Integer, Boolean>();

        for(int i=0; i<nums.length; i++){
            int current = nums[i];

            if(values.containsKey(nums[i])) return true;

            values.put(current, true);
        }
        
        return false;
    }
}
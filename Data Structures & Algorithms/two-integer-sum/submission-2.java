class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> valuesIndex = new HashMap<Integer,Integer>();

        for(int i=0; i<nums.length; i++){
            valuesIndex.put(nums[i],i);
        }

        for(int i=0; i<nums.length; i++){
            int newTarget = target-nums[i];
            if(valuesIndex.containsKey(newTarget) && valuesIndex.get(newTarget) != i )
                return (new int[] {i,valuesIndex.get(newTarget)});
        }
        return null;
    }
}

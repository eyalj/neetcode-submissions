class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int [] result = new int[k];
        int n = nums.length;
        HashMap<Integer,Integer> indexs = new HashMap<Integer,Integer>();
        HashMap<Integer,Integer> [] bucket = new HashMap[n+1];

        for(int i=0; i<=n; i++)
        {
            bucket[i] = new HashMap<Integer,Integer>();
        }

        for(int num: nums){
            indexs.putIfAbsent(num,0);
            int indexInBucket = indexs.get(num);
            bucket[indexInBucket].remove(num);
            bucket[indexInBucket+1].put(num,num);
            indexs.put(num,indexInBucket+1);
        }

        int numberOfValuesInResult = 0;

        for(int i = n; i >= 0; i--){
            if(bucket[i]!=null){
                for(Integer value : bucket[i].values()){
                    result[numberOfValuesInResult] = (int) value;
                    numberOfValuesInResult++;
                    if(numberOfValuesInResult == k) return result;
                }
            }
        }
        return result;
    }

}

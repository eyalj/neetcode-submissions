class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int [] a = new int[n];
        int [] b = new int[n];
        int [] result = new int[n];

        a[0] = 1;
        b[n - 1] = 1;

        for(int i=1,j=n-2;i<n && j>=0;i++,j--){
            a[i] = a[i-1] * nums[i-1];
            b[j] = b[j+1] * nums[j+1];
        }

        for(int i=0;i<n;i++){
            result[i] = a[i]*b[i];
        }

        return result;

    }
}  

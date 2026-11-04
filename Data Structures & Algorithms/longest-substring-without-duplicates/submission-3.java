class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character,Integer> word = new HashMap<Character,Integer>();
        int max = 0;
        int leftIndex=0;
        int rightIndex=0;
        while(leftIndex < s.length() && rightIndex < s.length()){
            char right = s.charAt(rightIndex);
            char left = s.charAt(leftIndex);
            
            if(!word.containsKey(right)){
                word.put(right,rightIndex);
                rightIndex++;
                continue;
            }
            max = Math.max(max,rightIndex-leftIndex);
            leftIndex = Math.max(leftIndex, word.get(right) + 1);
            word.put(right,rightIndex);
            rightIndex++;
        }

        return Math.max(max, rightIndex-leftIndex);
    }
}

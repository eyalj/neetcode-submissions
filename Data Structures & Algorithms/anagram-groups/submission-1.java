class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap <String, List<String>> groupAngram = new HashMap <String, List<String>>();
        List<List<String>> result = new ArrayList<List<String>>();


        for(int i=0; i<strs.length;i++){
            String counterKey = stringToCounterArray(strs[i]);
            groupAngram.putIfAbsent(counterKey, new ArrayList<>());
            groupAngram.get(counterKey).add(strs[i]);
        }

        for(List<String> group : groupAngram.values()){
            result.add(group);
        }
        return result;

    }

    private String stringToCounterArray(String s){
        int[] counter = new int[26];

        for(char current : s.toCharArray()){
            counter[current - 'a'] += 1;
        }

        return Arrays.toString(counter);
    }
}

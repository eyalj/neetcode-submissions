class Solution {

    public String encode(List<String> strs) {
        String code = new String();
        for(String str :strs){
            code = code.concat(String.valueOf(str.length())).concat("#").concat(str);
        }
        return code;
    }

    public List<String> decode(String str) {
        List <String> result = new ArrayList<String>();
        for(int i = 0; i<str.length();)
        {
            int hashIndex = str.indexOf("#",i);
            int sizeOfWord = Integer.parseInt(str.substring(i, hashIndex));
            String word = str.substring(hashIndex+1,hashIndex + sizeOfWord+1);
            result.add(word);
            i = hashIndex + 1 + sizeOfWord;
        }
        return result;
    }
}

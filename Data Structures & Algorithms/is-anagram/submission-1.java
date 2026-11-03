class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character,Integer> numberOfLetterInS = new HashMap<Character,Integer>();

        for (int i=0; i<s.length(); i++){
            Character currentChar = s.charAt(i);
            numberOfLetterInS.put(currentChar,numberOfLetterInS.getOrDefault(currentChar,0) + 1);
        }

        for(int i=0; i<t.length(); i++){
            Character currentChar = t.charAt(i);
            if(!numberOfLetterInS.containsKey (currentChar) || numberOfLetterInS.get(currentChar) <= 0) return false;
            numberOfLetterInS.put(currentChar, numberOfLetterInS.get(currentChar) - 1);
        }

        for (Character currentChar : numberOfLetterInS.keySet()){
            if(numberOfLetterInS.get(currentChar)!=0) return false;
        }

        return true;
        
    }
}

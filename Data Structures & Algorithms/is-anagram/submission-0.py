class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        number_of_latters_in_s = {}
        if(len(s)!=len(t)): return False
        for char in s:
            number_of_latters_in_s[char] = number_of_latters_in_s.get(char,0) + 1
        for char in t:
            number_of_latters_in_s[char] = number_of_latters_in_s.get(char,0) -1
        return all(count == 0 for count in number_of_latters_in_s.values())
 
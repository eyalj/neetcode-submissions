class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angrams = {}
        for word in strs:
            word_counter = [0] * 26 
            for char in word:
                word_counter[ord(char) - ord('a')] += 1
            key = tuple(word_counter)
            if(key not in angrams):
                angrams[key] = []
            angrams[key].append(word)
        return list(angrams.values())
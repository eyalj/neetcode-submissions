class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(0,len(strs)):
            strs[i] = str(len(strs[i])) + '|' + strs[i]
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        size_of_word = 0
        string_size_of_word = ''
        result = []
        for latter in s:
            if size_of_word == 0:
                if not latter == '|':
                    string_size_of_word +=latter 
                else:
                    result.append("")
                    size_of_word = int(string_size_of_word)
                    string_size_of_word = ''
            else:
                result[-1] += latter
                size_of_word -= 1
        return result
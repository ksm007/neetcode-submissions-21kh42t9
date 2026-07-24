class Trie:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, word:str):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.endOfWord = True


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                    return "".join(res)
            res.append(strs[0][i])
        
        return "".join(res)
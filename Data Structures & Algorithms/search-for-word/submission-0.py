
class Trie:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, word: str):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.endOfWord = True

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        root = Trie()
        root.addWord(word)
        ROWS, COLS = len(board), len(board[0])
        visit= set()
        def dfs(r,c,node):
            if (r <0 or c < 0 or r > ROWS -1 or c > COLS - 1 or (r,c) in visit or board[r][c] not in node.children):
                return False
            node = node.children[board[r][c]]
            if node.endOfWord:
                return True
            visit.add((r,c))
            found =  (dfs(r+1,c,node) or
            dfs(r-1,c,node) or
            dfs(r,c+1,node) or
            dfs(r,c-1,node))
            visit.remove((r,c))
            return found
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,root):
                    return True
        return False

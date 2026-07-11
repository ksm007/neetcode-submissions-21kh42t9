class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        nei = defaultdict(list)

        wordList.append(beginWord)

        for w in wordList:
            for j in range(len(w)):
                word = w[:j] + "*" + w[j+1:]
                nei[word].append(w)
        
        res = 1

        visited = set([beginWord])
        q = deque([beginWord])

        while q:
            for i in range(len(q)):
                currWord = q.popleft()
                if currWord == endWord:
                    return res
                for j in range(len(currWord)):
                    wildWord = currWord[:j] + "*" + currWord[j+1:]
                    for w in nei[wildWord]:
                        if w not in visited:
                            visited.add(w)
                            q.append(w)
            res+=1
        return 0

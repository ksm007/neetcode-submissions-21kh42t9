class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n1,n2 = len(s), len(p)
        memo = {}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i >= n1 and j >= n2:
                return True
            if j >= n2:
                return False
            match = i < n1 and (s[i] == p[j] or p[j] == ".")
            if j+1 < n2 and p[j+1] == "*":
                memo[(i,j)] = (match and dfs(i+1,j)) or dfs(i, j+2)
                return memo[(i,j)]
            if match:
                memo[(i,j)] =  dfs(i+1,j+1)
                return memo[(i,j)]
            memo[(i,j)] = False
            return False
        return dfs(0,0)
            
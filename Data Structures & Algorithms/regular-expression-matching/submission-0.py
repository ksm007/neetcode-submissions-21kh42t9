class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n1,n2 = len(s), len(p)

        def dfs(i,j):
            if i >= n1 and j >= n2:
                return True
            if j >= n2:
                return False
            match = i < n1 and (s[i] == p[j] or p[j] == ".")
            if j+1 < n2 and p[j+1] == "*":
                return (match and dfs(i+1,j)) or dfs(i, j+2)
            if match:
                return dfs(i+1,j+1)

            return False
        return dfs(0,0)
            
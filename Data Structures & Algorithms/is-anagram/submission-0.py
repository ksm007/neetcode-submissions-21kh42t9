class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a1, a2 = [0] *26, [0] * 26

        for c in s:
            a1[ord(c) - ord('a')]+=1
        for c in t:
            a2[ord(c) - ord('a')] +=1
        
        for i in range(len(a1)):
            if a1[i] != a2[i]:
                return False
        
        return True
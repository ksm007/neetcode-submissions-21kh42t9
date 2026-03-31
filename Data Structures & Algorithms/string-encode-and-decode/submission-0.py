class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        length = 0
        i = 0
        while i<len(s):
            j=i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            res.append(s[j+1:j+int(length)+1])
            i = j+1+length
        return res
            

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recur(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = recur(x*x,n//2)
            if n%2 == 1:
                return res *x
            return res
        po = recur(x,abs(n))
        return po if n>0 else 1/po
class CountSquares:

    def __init__(self):
        self.pts = list()
        self.pointMap = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pts.append(point)
        self.pointMap[tuple(point)] +=1

    def count(self, point: List[int]) -> int:
        res = 0
        px,py = point
        for x,y in self.pts:
            if(abs(x-px) != abs(y-py) or x==px and y==py):
                continue
            res += self.pointMap[(x,py)] * self.pointMap[(px,y)]

        return res 
